@app.route('/webhooks/grafana', methods=['OPTIONS', 'POST'])
@cross_origin()
@auth_required
def grafana():

    hook_started = webhook_timer.start_timer()
    alerts = parse_grafana(request.data)

    for incomingAlert in alerts:
        if g.get('customer', None):
            incomingAlert.customer = g.get('customer')

        add_remote_ip(request, incomingAlert)

        try:
            alert = process_alert(incomingAlert)
        except RejectException as e:
            webhook_timer.stop_timer(hook_started)
            return jsonify(status="error", message=str(e)), 403
        except Exception as e:
            webhook_timer.stop_timer(hook_started)
            return jsonify(status="error", message=str(e)), 500

        webhook_timer.stop_timer(hook_started)

    if alert:
        body = alert.get_body()
        body['href'] = absolute_url('/alert/' + alert.id)
        return jsonify(status="ok", id=alert.id, alert=body), 201, {'Location': body['href']}
    else:
        return jsonify(status="error", message="insert or update of grafana check failed"), 500

def parse_grafana(check):
    check = json.loads(check)
    timeout = 60

    alerts = []

    for item in check['evalMatches']:
        alerts.append(Alert(
            status='open',
            resource=item['metric'],
            event=check['state'],
            environment='Production',
            severity='critical',
            service=[check['ruleName']],
            text="Value:" + str(item['value']),
            origin='Grafana',
            event_type='Grafana_event',
            raw_data=item['value'],
            timeout=timeout,
            value='Error',
            group='group'
        ))

    return alerts

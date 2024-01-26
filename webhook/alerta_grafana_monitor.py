import json
from alerta.models.alert import Alert
from alerta.webhooks import WebhookBase
from dateutil.parser import parse as parse_date

class GrafanaWebhook(WebhookBase):
    """
    Grafana alerts webhook
    Example: https://grafana.com/docs/alerting/notifications/#webhook
    """

    def incoming(self, query_string, payload):
        # Add your Grafana-specific logic here
        # Example: extract information from payload for Grafana alerts

        # Placeholder values, modify according to your Grafana payload
        severity = 'firing'
        resource = 'GrafanaResource'
        event = 'GrafanaEvent'
        environment = 'Production'
        service = ['GrafanaService']
        group = 'GrafanaGroup'
        text = 'Grafana Alert'
        value = 'GrafanaValue'
        tags = []
        create_time = parse_date('2024-01-26T07:21:29')  # Replace with actual timestamp

        return Alert(
            resource=resource,
            event=event,
            environment=environment,
            severity=severity,
            service=service,
            group=group,
            value=value,
            text=text,
            tags=tags,
            attributes={},
            origin='Grafana',
            type='GrafanaAlert',
            create_time=create_time,
            raw_data=json.dumps(payload)
        )

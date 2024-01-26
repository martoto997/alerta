from setuptools import find_packages, setup

version = '5.0.2'

setup(
    name='alerta-grafana-monitor',
    version=version,
    description='Alerta webhook for Grafana',
    url='https://github.com/alerta/alerta-contrib',
    license='MIT',
    author='Martin Dinev',
    author_email='martoto999@gmail.com',
    packages=find_packages(),
    py_modules=['alerta_grafana_monitor'],  # Change the module name accordingly
    install_requires=[
        'python-dateutil'
    ],
    include_package_data=True,
    zip_safe=True,
    entry_points={
        'alerta.webhooks': [
            'grafanamonitor = alerta_grafana_monitor:GrafanaMonitorWebhook'  # Change the module and class name accordingly
        ]
    }
)

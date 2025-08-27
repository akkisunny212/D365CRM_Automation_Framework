import sys
from behavex import BehaveXRunner

if __name__ == '__main__':
    tags = sys.argv[1] if len(sys.argv) > 1 else ''
    BehaveXRunner(
        features_dir='features',
        steps_dir='steps',
        tags=tags,
        allure_report_dir='reports/allure',
        html_report_dir='reports/html'
    ).run()

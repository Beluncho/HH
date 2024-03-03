import requests
from pprint import pprint
msc_sal_have = []
sal_from = []
sal_to = []
def vac(results):
    for result in results['items']:
        if result['salary']:
            # pprint(result['id'])
            # pprint(result['salary'])
            msc_sal_have.append(result['id'])

            if result['salary']['from']:
                sal_from.append(result['salary']['from'])

                down_count = sum(sal_from) / len(sal_from)

            if result['salary']['to']:
                sal_to.append(result['salary']['to'])

                up_count = sum(sal_to) / len(sal_to)
    count = (up_count + down_count) / 2

    return count
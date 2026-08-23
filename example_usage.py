from client import ToxinFreeCookwareSustainableDtcCatalogClient

def main():
    client = ToxinFreeCookwareSustainableDtcCatalogClient()
    res = client.recommend_natural_cookware('healthy_slow_cooking')
    print('Toxin-Free Guarantee: ' + res['chemical_toxin_free_guarantee'])
    print('Packaging: Plastic Neutral ' + str(res['plastic_neutral_packaging']))
    for p in res['recommended_catalog']:
        print('  [' + p['sku'] + '] ' + p['material'] + ' (INR ' + str(p['price_inr']) + ')')
        print('    Benefit: ' + p['health_benefit'])

if __name__ == '__main__':
    main()

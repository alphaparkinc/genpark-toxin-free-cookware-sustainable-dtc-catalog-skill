class ToxinFreeCookwareSustainableDtcCatalogClient:
    def recommend_natural_cookware(self, cooking_style='daily_indian', stovetop_type='induction_and_gas'):
        products = [
            {
                'sku': 'IV_CAST_IRON_KADAI_28CM',
                'material': '100% Pre-Seasoned Pure Cast Iron',
                'health_benefit': 'Natural Iron Enrichment, 0% Chemical PTFE/PFOA',
                'lifetime_durability_years': 50,
                'price_inr': 1899.0,
                'compatibility': ['Gas', 'Induction', 'Campfire']
            }
        ]
        return {
            'cooking_style': cooking_style,
            'recommended_catalog': products,
            'chemical_toxin_free_guarantee': '100% Lead, Cadmium & Teflon Free',
            'plastic_neutral_packaging': True
        }

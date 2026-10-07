```python
"""
Comparative Life-Cycle Assessment (LCA) Calculator
Standard HMA vs. Nano-Modified Warm Mix Asphalt (WMA)
Author: Syed Nafiz Reja Hasib
"""

import pandas as pd

class AsphaltLCA:
    def __init__(self):
        # Baseline Emission Factors (kg CO2e per kg of material)
        self.ef_bitumen = 0.420
        self.ef_aggregate = 0.004
        self.ef_nanosilica = 4.300
        
        # Plant Heating Emissions (kg CO2e per tonne of mix)
        self.ef_hma_heating = 36.510
        self.ef_wma_heating = 29.054

    def calculate_hma(self):
        """Calculates Cradle-to-Gate GWP for 1 tonne of Standard HMA"""
        agg_impact = 950 * self.ef_aggregate
        bitumen_impact = 50 * self.ef_bitumen
        heating_impact = self.ef_hma_heating
        
        total_gwp = agg_impact + bitumen_impact + heating_impact
        return total_gwp

    def calculate_nano_wma(self):
        """Calculates Cradle-to-Gate GWP for 1 tonne of Nano-Modified WMA"""
        # Assumes 2% nano-silica by weight of binder (1 kg per tonne of mix)
        agg_impact = 949 * self.ef_aggregate
        bitumen_impact = 50 * self.ef_bitumen
        nano_impact = 1 * self.ef_nanosilica
        heating_impact = self.ef_wma_heating
        
        total_gwp = agg_impact + bitumen_impact + nano_impact + heating_impact
        return total_gwp

    def generate_report(self, standard_service_life=20, nano_extension_factor=1.15):
        """Generates a comparative analysis including annualized impacts"""
        hma_gwp = self.calculate_hma()
        nano_gwp = self.calculate_nano_wma()
        
        # Production difference
        prod_reduction_pct = ((hma_gwp - nano_gwp) / hma_gwp) * 100
        
        # Annualized Life-Cycle Impact
        hma_annual = hma_gwp / standard_service_life
        nano_annual = nano_gwp / (standard_service_life * nano_extension_factor)
        annual_reduction_pct = ((hma_annual - nano_annual) / hma_annual) * 100
        
        # Compile Results
        results = {
            "Metric": [
                "Cradle-to-Gate GWP (kg CO2e/t)", 
                "Estimated Service Life (Years)", 
                "Annualized GWP (kg CO2e/t/year)",
                "Carbon Reduction (%)"
            ],
            "Conventional HMA": [
                round(hma_gwp, 2), 
                standard_service_life, 
                round(hma_annual, 2),
                "Baseline"
            ],
            "Nano-Modified WMA": [
                round(nano_gwp, 2), 
                round(standard_service_life * nano_extension_factor, 1), 
                round(nano_annual, 2),
                f"-{round(annual_reduction_pct, 1)}%"
            ]
        }
        
        df = pd.DataFrame(results)
        print("\n=== LIFE-CYCLE ASSESSMENT: HMA vs NANO-WMA ===")
        print(df.to_string(index=False))
        print("==============================================\n")
        print(f"Insight: While production emissions drop by {round(prod_reduction_pct, 1)}%, ")
        print(f"the 15% durability multiplier drives a {round(annual_reduction_pct, 1)}% reduction in annualized carbon impact.")

if __name__ == "__main__":
    lca_model = AsphaltLCA()
    lca_model.generate_report()

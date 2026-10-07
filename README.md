# Nano-Modified Warm Mix Asphalt: LCA Calculator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

An open-source, screening Life-Cycle Assessment (LCA) tool designed to quantify the environmental benefits of integrating nano-additives (e.g., nano-silica) into Warm Mix Asphalt (WMA). 

## Overview
While Warm Mix Asphalt (WMA) significantly reduces production temperatures and energy consumption, nano-modification is required to mitigate its inherent moisture susceptibility[cite: 100]. This calculator evaluates whether the embodied carbon penalty of manufacturing nanomaterials is offset by the reduced heating demands of WMA and the extended service life of the pavement.

This script performs a cradle-to-gate (A1-A3) Global Warming Potential (GWP) calculation and applies a "Durability Multiplier" based on a conservative 15% service-life extension.

## Key Findings (Validated by this Model)
* **Production Savings:** Lowers initial cradle-to-gate GWP from 61.31 to 58.15 kg CO2e/t (-5.2%)[cite: 3].
* **Life-Cycle Savings:** Extending service life by 15% due to enhanced moisture resistance yields an annualized carbon reduction of 17.5%[cite: 3].

## Usage
Run the script to generate the comparative environmental metrics and output a structured results table.
```bash
python lca_calculator.py

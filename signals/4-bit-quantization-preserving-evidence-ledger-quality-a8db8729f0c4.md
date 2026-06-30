# 4-bit quantization preserving evidence-ledger quality

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `4-bit-quantization-preserving-evidence-ledger-quality-a8db8729f0c4`
Run ID: `4-bit-quantization-preserving-evidence-ledger-quality-a8db8729f0c4-20260619T144052024201+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/32d194b9714d

## What looked useful

Across 400 examples per condition, evidence-id exact match changed from 0.9775 baseline to 0.9950 quantized, while answer F1 dropped from 0.6800 to 0.6304 and joint answer+evidence exact dropped from 0.4650 to 0.4275. Source localization looked robust in this proxy, but answer quality degraded consistently.

## Boundaries and scale limits

Five synthetic 80-example seeds, one DistilBERT QA model, short CUDA runs, dequantized simulated 4-bit weights rather than production packed kernels, no real evidence-ledger corpus, no long-context or generative ledger evaluation.

## Claim scope

In a synthetic extractive evidence-ledger QA proxy using distilbert-base-cased-distilled-squad, simulated row-wise symmetric 4-bit post-training quantization preserved evidence-id localization but did not preserve answer text quality at parity.

## Why it stopped

Proxy-only early result: the hypothesis is not broadly validated because the synthetic extractive test showed preserved evidence-id localization but consistent answer-quality degradation.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded direct follow-up on a real or manually curated evidence-ledger benchmark with a stronger ledger model and real NF4/GPTQ/AWQ-style 4-bit quantizers.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-ledger 4-bit quantization test for source localization versus answer quality
- Success threshold: Evidence-id exact match drops by no more than 2 percentage points from the unquantized baseline while answer F1 drop is separately quantified with confidence intervals over at least 300 real or curated ledger examples.
- Stop condition: Stop if the unquantized baseline cannot reach at least 80% evidence-id exact and 70% answer F1, or if all tested 4-bit quantizers drop evidence-id exact by more than 5 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-quantization-preserving-evidence-ledger-quality-a8db8729f0c4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# Quantized Residual Gradients for Home Federated Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `quantized-residual-gradients-for-home-federated-pretraining-5a9f4d73fe71`
Run ID: `quantized-residual-gradients-for-home-federated-pretraining-5a9f4d73fe71-20260527T104621287955+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9544abdcc655

## What looked useful

4-bit residual gradients recovered fp32-like loss in the local proxy: mean q_residual-minus-fp32 final validation-loss gap was -0.0000046 across three seeds at 7.984x byte reduction, while q_no_residual lagged fp32 by +0.0036073. A 2-bit seed-7 stress test was mixed: compressed training stayed close to fp32 at 15.937x byte reduction, but residuals did not beat no-residual final loss.

## Boundaries and scale limits

Synthetic Markov token data, tiny 2-layer width-64 Transformer, 8 synchronous clients, one local gradient batch per client per round, no real tokenizer corpus, no secure aggregation or privacy noise, no unreliable home networking, no client dropout, and no GPT-2-small-class or larger validation.

## Claim scope

In a tiny synthetic non-IID federated Transformer language-model proxy, 4-bit client gradient quantization with persistent residual error feedback matched fp32 validation loss over 120 rounds across seeds 7, 11, and 13 while reducing transmitted gradient bytes by 7.984x; same-budget 4-bit quantization without residuals showed a repeatable small validation-loss penalty.

## Why it stopped

No-paper closure: this run produced useful local proxy evidence for the residual-gradient mechanism, but not direct real home federated pretraining evidence.

## Recommended next action

Run a bounded deepen follow-up on a real tokenizer corpus with client dropout and a GPT-2-small-class or parameter-matched small Transformer, predeclaring a validation-perplexity tolerance and effective uplink accounting.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Corpus Federated LM Test of 4-bit Residual Gradient Uplink Compression
- Success threshold: 4-bit residual final validation perplexity within 0.1% of fp32 and better than 4-bit no-residual by at least 0.2% relative perplexity, with at least 6x effective client uplink reduction.
- Stop condition: Stop if 4-bit residual is worse than fp32 by more than 0.5% relative validation perplexity after the planned training budget, or if effective overhead reduces uplink savings below 4x.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-residual-gradients-for-home-federated-pretraining-5a9f4d73fe71`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

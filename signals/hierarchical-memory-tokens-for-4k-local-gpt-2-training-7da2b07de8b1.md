# Hierarchical memory tokens for 4k local GPT-2 training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `hierarchical-memory-tokens-for-4k-local-gpt-2-training-7da2b07de8b1`
Run ID: `hierarchical-memory-tokens-for-4k-local-gpt-2-training-7da2b07de8b1-20260524T080336170772+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/868b1785ee47

## What looked useful

Hierarchical memory tokens gave a clear optimization and efficiency advantage on a 4k-context mechanism probe: HMT reached 99.9% accuracy by step 1200 and 100% by step 1400, using about 1.49 GiB CUDA allocation, while full attention was still 6.64% at step 1200 with about 2.55 GiB allocation and much lower throughput.

## Boundaries and scale limits

Proxy-only synthetic retrieval; not natural text, not full causal GPT-2 language-model training, not parameter-matched GPT-2-small, not multi-seed, and not publication-grade robustness evidence.

## Claim scope

On a synthetic 4096-token block-retrieval probe, a small hierarchical-memory-token model learned to route a final query through 16 chunk memories and reached 100% eval accuracy, while local-tail and naive full-attention controls stayed near chance under bounded local training budgets.

## Why it stopped

Stopped after producing a bounded proxy mechanism result; the evidence is useful but insufficient for a paper or direct validation of 4k local GPT-2 training.

## Recommended next action

Run a parameter-matched mini-GPT-2 4k-context language-model experiment on a small real corpus with dense attention, local attention, and HMT controls across at least 3 seeds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Parameter-matched mini-GPT-2 HMT language-model validation
- Success threshold: HMT beats the local-attention baseline by at least 5% relative validation perplexity or at least 10 absolute points on a held-out long-range retrieval diagnostic without worse throughput/memory than the dense/full attention control.
- Stop condition: Stop as negative if HMT fails to beat local attention on both perplexity and retrieval diagnostics in 3 seeds, or if it requires more memory/wall-clock than dense/full attention at the same parameter scale.

## Evidence references

- Artifact root: `<local-path>/projects/hierarchical-memory-tokens-for-4k-local-gpt-2-training-7da2b07de8b1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# Real-corpus tiny GPT-2 domain mixture ratio sweep

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-corpus-tiny-gpt-2-domain-mixture-ratio-sweep-1e0e21317a`
Run ID: `real-corpus-tiny-gpt-2-domain-mixture-ratio-sweep-1e0e21317a-20260621T085959432641+0000`

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

- Parent run decision: Domain mixture ratio sweep for tiny GPT-2 pretraining: enoch://control-plane/projects/domain-mixture-ratio-sweep-for-tiny-gpt-2-pretraining-c49b19bab936/runs/domain-mixture-ratio-sweep-for-tiny-gpt-2-pretraining-c49b19bab936-20260621T084956606540+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/094f0ceaee0d

## What looked useful

Best interior ratio 0.50 improved mean balanced validation loss by 5.04% over the best endpoint; all three seeds exceeded the predeclared 1% threshold.

## Boundaries and scale limits

Tiny model, short training horizon, two English text domains, one tokenizer, no GPT-2-small-class baseline, no convergence-length ablation, and no broader domain robustness test.

## Claim scope

In a controlled small direct test on AG News and WikiText-2, a 3.3M-parameter GPT-2-style causal LM trained from scratch for 240 steps per ratio achieved lower balanced validation loss with an interior 50/50 domain mixture than with either single-domain endpoint across three seeds.

## Why it stopped

Tier 1 direct evidence supports the mechanism but is too small and short for publication readiness.

## Recommended next action

Run a bounded deepen follow-up at GPT-2-small-class or medium tiny scale with longer training, three or more seeds, and the same interior-versus-endpoint balanced-loss threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small-class real-corpus domain mixture ratio confirmation
- Success threshold: Best interior ratio achieves at least 1% lower mean balanced validation loss than the best endpoint, with the advantage present in at least two of three seeds and no single domain catastrophically worse than both endpoints.
- Stop condition: Stop if no interior ratio beats the best endpoint by 1% mean balanced validation loss after the calibrated longer training budget, or if the effect reverses in two or more seeds.

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-tiny-gpt-2-domain-mixture-ratio-sweep-1e0e21317a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

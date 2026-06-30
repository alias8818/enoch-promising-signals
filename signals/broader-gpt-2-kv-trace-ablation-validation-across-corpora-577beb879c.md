# Broader GPT-2 KV-trace ablation validation across corpora and model sizes

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `28`
Project ID: `broader-gpt-2-kv-trace-ablation-validation-across-corpora-577beb879c`
Run ID: `broader-gpt-2-kv-trace-ablation-validation-across-corpora-577beb879c-20260522T211408270261+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `28`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -10, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Real GPT-2 KV-trace test of causal attention x residual allocation against norm allocation: enoch://control-plane/projects/real-gpt-2-kv-trace-test-of-causal-attention-x-residual-al-60f60ea257/runs/real-gpt-2-kv-trace-test-of-causal-attention-x-residual-al-60f60ea257-20260522T210402648424+0000
- Parent run decision: Causal attention-predicted residual KV allocation with metadata-inclusive bit budget: enoch://control-plane/projects/causal-attention-predicted-residual-kv-allocation-with-met-23e9d18730/runs/causal-attention-predicted-residual-kv-allocation-with-met-23e9d18730-20260522T205711963114+0000

## What looked useful

Across 12 non-tiny model/corpus/fraction conditions, KV-trace-top ablation never exceeded KV-trace-bottom ablation in loss damage. Mean trace_top minus trace_bottom delta-loss was -0.9466, and trace_top beat the five-draw random-control mean in only 2 of 12 conditions.

## Boundaries and scale limits

Models were limited to sshleifer/tiny-gpt2, distilgpt2, and gpt2; robustness metrics emphasize distilgpt2 and gpt2. Corpora were fixed local text mixtures rather than full external benchmark corpora. This does not rule out alternative KV-trace definitions, larger GPT-2 variants, or training-time interventions.

## Claim scope

For the concrete activation KV-trace statistic implemented here, high KV-trace attention heads are not robustly more causally important under evaluation-time head-mask ablation on GPT-2-small-class pretrained models across local wiki/news/code text mixtures.

## Why it stopped

Moderate bounded direct evidence falsified the tested KV-trace-top ablation success pattern; this is not full benchmark-scale validation, but it is sufficient to reject scaling this exact statistic as a paper-readiness candidate.

## Recommended next action

Stop this follow-up as a no-paper negative/useful-signal result; follow-up depth is 4, and the bounded direct evidence contradicts the proposed top-KV-trace ranking direction.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/broader-gpt-2-kv-trace-ablation-validation-across-corpora-577beb879c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

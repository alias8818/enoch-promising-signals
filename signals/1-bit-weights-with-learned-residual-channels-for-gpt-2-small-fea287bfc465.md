# 1-bit Weights with Learned Residual Channels for GPT-2-small

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `1-bit-weights-with-learned-residual-channels-for-gpt-2-small-fea287bfc465`
Run ID: `1-bit-weights-with-learned-residual-channels-for-gpt-2-small-fea287bfc465-20260522T145405321199+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/bd4403e6afb2

## What looked useful

Residual channels did not materially improve validation loss over the plain 1-bit STE control: rank 8 improved mean loss by 0.00095 versus seed-to-seed standard deviation near 0.033 while adding 32768 parameters; rank 32 improved mean loss by 0.00020 while adding 131072 parameters and reducing throughput substantially.

## Boundaries and scale limits

Not GPT-2-small scale, not natural language pretraining, no downstream tasks, and no production 1-bit inference kernel. Results are an early mechanism falsification only.

## Claim scope

Bounded GPT-style synthetic autoregressive proxy with 2-layer 128-width transformer, 3 seeds, 800 training steps, comparing dense linears, 1-bit STE linears, and 1-bit STE linears plus learned low-rank residual channels at ranks 8 and 32.

## Why it stopped

Proxy/early falsification: the tested residual-channel mechanism failed to produce a meaningful quality gain over plain 1-bit STE controls at ranks 8 or 32, and the evidence is not a full GPT-2-small validation.

## Recommended next action

Stop this line as a no-paper proxy/early falsification unless a future direct GPT-2-small real-text experiment can show a materially larger residual-channel benefit over a plain 1-bit control.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/1-bit-weights-with-learned-residual-channels-for-gpt-2-small-fea287bfc465`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

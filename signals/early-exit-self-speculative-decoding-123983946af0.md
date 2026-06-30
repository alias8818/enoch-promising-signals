# Early-Exit Self-Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `early-exit-self-speculative-decoding-123983946af0`
Run ID: `early-exit-self-speculative-decoding-123983946af0-20260521T215224640347+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/ea20a1ed6703

## What looked useful

Cheap early exits had low exact top-1 agreement, while accurate later exits cost too much. GPT-2 small's best measured speculative speedup was 0.710x and its best idealized layer-fraction speedup was 0.980x, both below break-even. DistilGPT-2's best measured speedup was 0.583x.

## Boundaries and scale limits

This was a bounded local probe, not a production KV-cache decoder or broad benchmark. It did not train auxiliary heads, test stochastic exact speculative sampling, evaluate larger model families, or use a large prompt corpus.

## Claim scope

On pretrained DistilGPT-2 and GPT-2 small with untrained intermediate exits using the final layer norm and tied LM head, greedy early-exit self-speculative drafting did not reach break-even speedup on 32 fixed prompts and 768 generated positions per model.

## Why it stopped

Proxy/local early falsification: the directly tested untrained GPT-2-class early exits failed to reach break-even under exact greedy agreement and measured partial-forward cost, but this is not a full validation of trained-head or production serving variants.

## Recommended next action

Do not scale the untrained intermediate-exit method as-is; run one bounded follow-up that trains or calibrates auxiliary exit heads and requires measured speedup above 1.10x before any larger serving benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Train calibrated auxiliary early-exit heads for GPT-2 self-speculative drafting
- Success threshold: At least one exit/gamma setting achieves measured speedup > 1.10x on held-out prompts with exact greedy output matching and no hidden verifier-cost omission.
- Stop condition: Stop if trained/calibrated exits remain below 0.95x measured speedup or if cheap exits below half depth remain under 0.45 exact top-1 agreement on held-out prompts.

## Evidence references

- Artifact root: `<local-path>/projects/early-exit-self-speculative-decoding-123983946af0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

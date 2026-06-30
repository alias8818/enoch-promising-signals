# Activation-Cache Linear Probe Self-Draft

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `activation-cache-linear-probe-self-draft-67d16f3032cc`
Run ID: `activation-cache-linear-probe-self-draft-67d16f3032cc-20260610T122831764177+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b835979da057

## What looked useful

Activation-cache linear probes are promising for one-step target-model imitation but this bounded run does not support a direct multi-token self-draft claim; true t+2 top-1 stayed around 0.019 to 0.027.

## Boundaries and scale limits

Single small pretrained model, teacher-forced WikiText-2 contexts, offline linear probes only. No online speculative decoding, generated-context rollout, latency speedup measurement, confidence thresholding, larger model, or multi-token accepted-draft validation was run.

## Claim scope

On distilgpt2 with WikiText-2 held-out examples, linear probes over cached hidden states can imitate the frozen model's one-step greedy next-token choice substantially above simple baselines, with best layer-5 greedy-match top-1 0.5248 and top-20 0.7243.

## Why it stopped

No-paper closure: bounded local evidence supports only a one-step imitation mechanism; it does not validate multi-token self-drafting or real decoding speedup.

## Recommended next action

Run a bounded online decoding follow-up that attaches the best layer-5 greedy probe to distilgpt2, drafts one token with confidence thresholds, verifies against the frozen model, and reports acceptance-adjusted latency versus ordinary greedy decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Online One-Token Probe-Draft Verification for DistilGPT2
- Success threshold: At least 1.10x wall-clock tokens/sec improvement over ordinary greedy decoding on the same GB10 host while preserving identical verified greedy output for accepted/rejected probe paths, with acceptance rate at or above 40% after thresholding.
- Stop condition: Stop if acceptance-adjusted throughput is below 1.00x baseline or if verification overhead erases speedup across all tested confidence thresholds.

## Evidence references

- Artifact root: `<local-path>/projects/activation-cache-linear-probe-self-draft-67d16f3032cc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

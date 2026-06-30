# KV-Intervention Anchor Retention Mechanism Probe

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `kv-intervention-anchor-retention-mechanism-probe-da67b2b4f0`
Run ID: `kv-intervention-anchor-retention-mechanism-probe-da67b2b4f0-20260530T010603434551+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Real-Model Exact Anchor KV Retention Probe: enoch://control-plane/projects/real-model-exact-anchor-kv-retention-probe-73b6b05056/runs/real-model-exact-anchor-kv-retention-probe-73b6b05056-20260529T170213155820+0000
- Parent run decision: Baseline-Normalized Multi-Model Anchor KV Retention Probe: enoch://control-plane/projects/baseline-normalized-multi-model-anchor-kv-retention-probe-c24e2a7999/runs/baseline-normalized-multi-model-anchor-kv-retention-probe-c24e2a7999-20260529T203813889134+0000

## What looked useful

Across seeds 0/1/2 at 24 distractors, baseline accuracy was 1.0000, anchor-zero accuracy was 0.0119 +/- 0.0044, matched distractor-zero accuracy was 1.0000, and clean anchor K/V restoration improved corrupt-anchor accuracy by 0.9860 +/- 0.0013. At 48/96 distractors the intervention direction persisted, but baseline accuracy averaged only 0.1359 and 0.1569 with high seed variance.

## Boundaries and scale limits

Evidence is synthetic and small-model only. It does not cover natural language, pretrained transformers, GPT-2-small-class baselines, 7B+ models, production long-context attention, or robust length extrapolation. At 48/96 distractors, baseline accuracy was low and seed-dependent because training used 24 distractors.

## Claim scope

In a 4-layer synthetic causal transformer trained on a 24-distractor anchor-copy associative-recall task, cached K/V vectors at the anchor pair are causally necessary and sufficient for trained-length retrieval: anchor K/V zeroing or shuffling collapses accuracy to chance, matched distractor K/V zeroing does not, and clean anchor K/V restoration fully recovers corrupt-anchor inputs.

## Why it stopped

Moderate direct synthetic evidence supports trained-length anchor K/V causality, but long-context retention was mixed and not robust enough for publication-grade closure.

## Recommended next action

Stop this run as no-paper useful signal; the concrete next bounded test is a length-curriculum replication that requires high 96-distractor baseline accuracy before claiming anchor retention.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Length-Curriculum Anchor K/V Retention Replication
- Success threshold: Across at least three seeds, baseline accuracy at 96 distractors is >=0.80, anchor-zero accuracy delta is >=0.60, matched distractor-zero delta is <=0.10, and clean-anchor restoration recovers >=80% of the corrupt-anchor accuracy loss.
- Stop condition: Stop as negative if 96-distractor baseline accuracy stays below 0.50 after a length curriculum, or if anchor ablation is not at least 3x larger than the matched distractor control when baseline accuracy is >=0.80.

## Evidence references

- Artifact root: `<local-path>/projects/kv-intervention-anchor-retention-mechanism-probe-da67b2b4f0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

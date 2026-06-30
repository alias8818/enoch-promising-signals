# 4-bit Quantized Volunteer Training with Bounded Cheating Surface

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `4-bit-quantized-volunteer-training-with-bounded-cheating-surface-bc2c0e9e13b3`
Run ID: `4-bit-quantized-volunteer-training-with-bounded-cheating-surface-bc2c0e9e13b3-20260614T020148740909+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e68f043f16b4

## What looked useful

4-bit gradient transport was not the bottleneck in the toy task, and replay audit is a strong per-claim predicate, but sampled audit alone does not bound unaudited cheating. At 70% malicious updates, 25% audit detected audited cheats but did not recover accuracy; 100% audit removed nearly all malicious updates but still undertrained because rejected work was not replaced.

## Boundaries and scale limits

Synthetic convex binary classification only; no LLM, GPT-2-small, QLoRA, privacy, Sybil resistance, heterogeneous volunteer hardware, network, cryptographic, or datacenter-scale evidence. Audit assumes the coordinator can recompute exact claimed minibatches.

## Claim scope

In a bounded NumPy logistic-regression proxy, clipped signed 4-bit volunteer gradient transport matched dense-gradient training accuracy, and coordinator replay-audit detected nearly all audited malicious quantized gradient claims when exact minibatch replay was available.

## Why it stopped

No-paper useful signal: local proxy evidence supports 4-bit transport and replay-audit detection, but early adversarial stress falsifies the stronger claim that sampled audit alone provides a complete bounded cheating surface.

## Recommended next action

Run a bounded deepen test that adds replacement work or reputation-weighted scheduling to the audit protocol on a tiny transformer or GPT-2-small-class proxy, then compare against dense/standard and no-audit controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Audit plus replacement scheduling for 4-bit volunteer training
- Success threshold: Under at least 30% malicious volunteer updates, audit plus replacement/reputation recovers at least 95% of the honest 4-bit baseline quality while keeping audited-cheat detection above 99% and false rejects below 1%.
- Stop condition: Stop if the mitigation cannot outperform sampled-audit-only quality by at least 2 percentage points or equivalent loss improvement under the same adversarial rate, or if coordinator replay cost exceeds the saved volunteer compute in the bounded setup.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-quantized-volunteer-training-with-bounded-cheating-surface-bc2c0e9e13b3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

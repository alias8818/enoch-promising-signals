# Real Tiny-Model Evidence Ledger QA Probe

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `real-tiny-model-evidence-ledger-qa-probe-c6fd52f482`
Run ID: `real-tiny-model-evidence-ledger-qa-probe-c6fd52f482-20260525T020641647359+0000`

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

- Parent run decision: Evidence Ledger for Tiny Local Agents: enoch://control-plane/projects/evidence-ledger-for-tiny-local-agents-7b0d6d45e8f9/runs/evidence-ledger-for-tiny-local-agents-7b0d6d45e8f9-20260524T235620269272+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/f7b1369e92e7

## What looked useful

Raw prose context achieved 95.0% accuracy and 5.0% unsupported wrong-color rate; the evidence ledger achieved 76.7% accuracy and 21.7% unsupported wrong-color rate. The ledger broke 13 cases raw prose got right and recovered only 2 raw-prose misses.

## Boundaries and scale limits

Single 0.5B instruction model, one ledger serialization, synthetic color/object QA, CPU inference only, no retrieval pipeline, no naturalistic corpus, no training, and no larger-model replication.

## Claim scope

On 60 controlled one-hop synthetic QA cases using cached Qwen/Qwen2.5-0.5B-Instruct, a semicolon-delimited evidence ledger with one relevant row and one distractor row did not improve extractive answer accuracy over the same facts in raw prose.

## Why it stopped

Direct small real-model QA test missed the success threshold: ledger accuracy was 18.33 percentage points below raw prose and unsupported wrong-color rate was 16.67 percentage points higher, so this is an early falsification rather than full validation.

## Recommended next action

Stop this follow-up as a direct Tier 1 early falsification of the stated ledger-over-raw threshold; any new work should first ablate ledger serialization before considering scale.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/real-tiny-model-evidence-ledger-qa-probe-c6fd52f482`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

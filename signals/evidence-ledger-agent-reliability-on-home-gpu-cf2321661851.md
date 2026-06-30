# Evidence-Ledger Agent Reliability on Home GPU

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `evidence-ledger-agent-reliability-on-home-gpu-cf2321661851`
Run ID: `evidence-ledger-agent-reliability-on-home-gpu-cf2321661851-20260612T050100640242+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/310bf9c9a430

## What looked useful

Citation-looking outputs were not reliable grounding evidence. Ledger prompting increased unsupported answer rate by 0.583 for Qwen2.5-0.5B-Instruct and 0.683 for Qwen2.5-1.5B-Instruct relative to plain evidence prompting.

## Boundaries and scale limits

Synthetic short-context tasks only; two small local models only; no real agent traces, no long-context ledgers, no deterministic verifier/retry loop, and no 7B+ or frontier model validation.

## Claim scope

On a deterministic 60-task synthetic evidence-packet benchmark run locally on GB10, prompt-only evidence-ledger formatting with citation requirements reduced grounded-answer reliability versus plain evidence prompting for cached Qwen2.5 0.5B and 1.5B instruct models.

## Why it stopped

Corrected local evidence falsified the scoped prompt-only evidence-ledger hypothesis; this is a bounded synthetic negative/useful signal rather than full real-agent validation.

## Recommended next action

Stop this prompt-only ledger run; next test should add a deterministic citation verifier and retry policy, then compare against the same plain baseline on this benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Verifier-Gated Evidence Ledger Reliability Probe
- Success threshold: Verifier-gated ledger unsupported rate at least 0.20 lower than prompt-only ledger and no worse than plain prompting by more than 0.05 absolute accuracy on both tested models.
- Stop condition: Stop if verifier-gated ledger still has higher unsupported rate than plain prompting on either model or if retry overhead exceeds 3x mean plain latency without reliability gain.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-reliability-on-home-gpu-cf2321661851`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

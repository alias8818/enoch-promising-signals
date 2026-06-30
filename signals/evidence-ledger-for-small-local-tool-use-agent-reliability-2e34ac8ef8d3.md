# Evidence ledger for small local tool-use agent reliability

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `evidence-ledger-for-small-local-tool-use-agent-reliability-2e34ac8ef8d3`
Run ID: `evidence-ledger-for-small-local-tool-use-agent-reliability-2e34ac8ef8d3-20260527T222710948931+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/0baf61e57fbd

## What looked useful

On simple conflict traces both baseline and ledger prompts saturated at 24/24 correct. On abstention stress traces both scored 10/12 and failed on the same stale-value cases. Ledger prompting added small latency and produced no measured reliability gain.

## Boundaries and scale limits

One local model, synthetic traces, single deterministic seed, short outputs, no live tool execution, and no implementation-enforced ledger/gating policy. This does not rule out benefits from externalized ledgers, harder long-context traces, larger samples, or different models.

## Claim scope

Prompt-only evidence-ledger instructions did not improve Phi-4-mini GGUF reliability over a direct baseline on 24 synthetic current-record conflict tasks and 12 synthetic missing-evidence abstention tasks run locally with deterministic decoding.

## Why it stopped

Proxy/local synthetic benchmarks found no prompt-only ledger advantage and shared abstention failures, so the result is useful no-paper evidence rather than publication-grade support.

## Recommended next action

Stop this run as a bounded null result; a separate follow-up should test an implementation-enforced evidence ledger that blocks unsupported final answers instead of relying on prompt-only compliance.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Implementation-enforced evidence ledger gating for local tool-use agents
- Success threshold: Enforced ledger reduces unsupported/stale rate by at least 50% relative to prompt-only ledger without reducing answerable-task accuracy by more than 5 percentage points.
- Stop condition: Stop if enforced ledger fails to reduce unsupported/stale errors on the held-out synthetic abstention suite or if most failures come from parser/template brittleness rather than agent reliability.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-small-local-tool-use-agent-reliability-2e34ac8ef8d3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

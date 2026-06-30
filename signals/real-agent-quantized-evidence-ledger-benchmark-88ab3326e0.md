# Real-agent quantized evidence ledger benchmark

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-agent-quantized-evidence-ledger-benchmark-88ab3326e0`
Run ID: `real-agent-quantized-evidence-ledger-benchmark-88ab3326e0-20260529T041443417864+0000`

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

- Parent run decision: Tiny agent evidence ledger with quantized memory: enoch://control-plane/projects/tiny-agent-evidence-ledger-with-quantized-memory-0753f93fe197/runs/tiny-agent-evidence-ledger-with-quantized-memory-0753f93fe197-20260528T232413560894+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/862178abae9a

## What looked useful

QEL preserved all non-exact audit predicates in this benchmark, but failed the pre-registered full target: overall QEL relative accuracy was 0.875 versus the >=0.90 threshold because exact final-source recovery was impossible, and QEL size was 0.509 of raw versus the <=0.50 threshold.

## Boundaries and scale limits

Small deterministic micro-agent only; no LLM policy traces, production agent logs, adversarial audit questions, long workflows, or external reviewer-written audits.

## Claim scope

A controlled Tier 1 benchmark of four deterministic local command/edit/test agent episodes comparing raw transcripts against a lossy quantized evidence ledger on eight post-hoc audit predicates per episode.

## Why it stopped

Controlled Tier 1 direct benchmark falsified the stated threshold; this is not full validation, but it directly shows lossy QEL cannot satisfy exact provenance audit requirements under the tested design.

## Recommended next action

Stop this run as no-paper useful signal; test a hybrid QEL that stores selected exact diff/source capsules for provenance predicates while keeping quantized facts for coarse audit queries.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hybrid quantized ledger with exact diff capsules
- Success threshold: Hybrid QEL reaches >=0.95 relative raw-ledger accuracy overall, 1.00 exact-provenance recovery on selected final diffs/source snippets, and <=0.65 raw byte fraction.
- Stop condition: Stop if exact provenance remains unrecoverable or serialized size exceeds 0.70 of raw on the controlled episodes before adding larger traces.

## Evidence references

- Artifact root: `<local-path>/projects/real-agent-quantized-evidence-ledger-benchmark-88ab3326e0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

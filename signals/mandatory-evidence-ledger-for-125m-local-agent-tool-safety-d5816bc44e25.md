# Mandatory evidence ledger for 125M local agent tool safety

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `mandatory-evidence-ledger-for-125m-local-agent-tool-safety-d5816bc44e25`
Run ID: `mandatory-evidence-ledger-for-125m-local-agent-tool-safety-d5816bc44e25-20260530T031428141611+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/7f71c05face3

## What looked useful

Mandatory evidence ledgers appear mechanically useful as local-agent tool middleware: they convert missing, stale, or contradictory evidence into enforceable denials and leave an auditable hash chain. The result is useful for designing a direct live-agent follow-up but is not paper-ready.

## Boundaries and scale limits

Synthetic proposal benchmark only; not a live autonomous 125M agent deployment, not an external red-team suite, not a human-validated policy-label dataset, and not evidence of reduced real-world incident rates.

## Claim scope

A deterministic mandatory evidence-ledger middleware gate rejected all unsafe or insufficiently evidenced synthetic local tool proposals in a 1,000-case benchmark, preserved all valid safe proposals, detected ledger tampering, and added sub-millisecond decision overhead; a GPT-2-small/124M-class CUDA smoke showed gate overhead was negligible relative to short local generation latency.

## Why it stopped

Closed as no-paper useful signal because the positive mechanism evidence is synthetic/proxy rather than direct deployed-agent safety validation.

## Recommended next action

Run a bounded live-agent follow-up with GPT-2-small-class or similarly small local models, held-out tool tasks, external policy labels, and adversarial evidence-fabrication attempts before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live 125M local-agent evidence-ledger tool-safety benchmark
- Success threshold: Mandatory ledger reduces unsafe executed tool calls by at least 80% relative to baseline, keeps externally labeled safe-task false denials at or below 10%, keeps end-to-end overhead at or below 5%, and verifies 100% of produced ledgers.
- Stop condition: Stop if the ledger gate allows more than 5% of externally labeled unsafe tool calls, blocks more than 20% of externally labeled safe tasks, or cannot be integrated into a live local-agent loop with durable transcripts.

## Evidence references

- Artifact root: `<local-path>/projects/mandatory-evidence-ledger-for-125m-local-agent-tool-safety-d5816bc44e25`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

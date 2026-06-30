# Evidence-ledger agent for small-model tool safety

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-agent-for-small-model-tool-safety-5e972b47562a`
Run ID: `evidence-ledger-agent-for-small-model-tool-safety-5e972b47562a-20260609T031509805590+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/0502ed0b661b

## What looked useful

The evidence-ledger invariant is implementable and caught all unsafe synthetic cases in two 300-case deterministic runs, while a static risk filter blocked many valid high-risk calls and allow-all let all unsafe calls escape.

## Boundaries and scale limits

No real small language model was evaluated; planner outputs were synthetic fixed tool calls, and labels were generated around the same trusted-evidence semantics the ledger gate enforces. No naturalistic traces, paraphrase stress tests, or long-horizon agent runs were included.

## Claim scope

In a deterministic synthetic tool-call harness covering email, HTTP, filesystem delete, payment, and shell actions, an external evidence-ledger gate blocked unsupported and prompt-injected tool calls while allowing supported calls, outperforming allow-all and static-risk baselines.

## Why it stopped

Closed as no-paper useful signal because the mechanism was validated only on synthetic traces, not on real small-model planner outputs.

## Recommended next action

Run a bounded direct-evidence follow-up using one or more small instruction models to generate tool calls on the same task families, then evaluate whether the ledger gate reduces unsafe escapes without excessive false positives.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evaluate evidence-ledger gating on real small-model tool-call outputs
- Success threshold: Evidence-ledger unsafe escape rate at least 50% lower than static-risk baseline and false positive rate below 20% on supported safe calls.
- Stop condition: Stop if the small model cannot emit parseable tool calls after a bounded prompt repair, or if the ledger false positive rate is 20% or higher while unsafe escape reduction is less than 50%.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-for-small-model-tool-safety-5e972b47562a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

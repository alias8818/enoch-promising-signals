# Pre-registered Public Benchmark Confirmation of Evidence-Ledger Tool-Use Gating

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `pre-registered-public-benchmark-confirmation-of-evidence-l-759b8257ce`
Run ID: `pre-registered-public-benchmark-confirmation-of-evidence-l-759b8257ce-20260524T165526527601+0000`

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

- Parent run decision: Evidence-Ledger Constraint for Tiny Tool-Using Agents: enoch://control-plane/projects/evidence-ledger-constraint-for-tiny-tool-using-agents-4b5da8989cda/runs/evidence-ledger-constraint-for-tiny-tool-using-agents-4b5da8989cda-20260524T084003946062+0000
- Parent run decision: Real Tiny-LLM Evidence-Ledger Tool-Use Evaluation: enoch://control-plane/projects/real-tiny-llm-evidence-ledger-tool-use-evaluation-674a5c5e95/runs/real-tiny-llm-evidence-ledger-tool-use-evaluation-674a5c5e95-20260524T155210999317+0000

## What looked useful

At tool reliability 0.45, invalid accepts fell from 0.5488 for accept-first to 0.0291 with the evidence ledger and accuracy rose from 0.5776 to 0.6148. At reliability 0.65, invalid accepts fell from 0.3489 to 0.0160 and accuracy rose from 0.5927 to 0.6188. However, no-tool majority and ledger-no-retry controls matched or beat cost-adjusted utility, so the broader end-to-end value claim remains mixed.

## Boundaries and scale limits

Validation used simulated noisy tool outputs, one public yes/no QA benchmark, a lexical gate, and a lightweight Naive Bayes answerer; it did not test live LLM agents, multi-hop tool use, learned routers, or production tool traces.

## Claim scope

On a local BoolQ/SuperGLUE noisy passage-tool benchmark with fixed seeds, a lexical evidence-ledger gate sharply reduces unsupported tool-output acceptance and improves accuracy versus an accept-first tool-use baseline, but not cost-adjusted utility versus no-tool or no-retry controls.

## Why it stopped

Tier-2 validation produced useful mechanism evidence but failed the stricter paper gate because gains were limited to accept-first comparisons and did not beat no-tool or no-retry controls on cost-adjusted utility.

## Recommended next action

Run one bounded deepen follow-up using the same fixed-seed noisy-tool protocol but replace the NB answerer with a stronger public frozen QA/NLI model and add at least one multi-hop public benchmark before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Stronger Public Answerer Test for Evidence-Ledger Tool Gating
- Success threshold: Evidence-ledger gate must reduce invalid acceptance by at least 80% relative to accept-first and improve mean cost-adjusted utility by at least 0.02 over accept-first, no-tool, and no-retry controls on both public benchmarks.
- Stop condition: Stop if the stronger-answerer run again fails to beat no-tool or no-retry cost-adjusted utility on either benchmark, even if invalid acceptance improves.

## Evidence references

- Artifact root: `<local-path>/projects/pre-registered-public-benchmark-confirmation-of-evidence-l-759b8257ce`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

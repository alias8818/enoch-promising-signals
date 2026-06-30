# Ledger Consensus Decoding for Tool Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ledger-consensus-decoding-for-tool-agents-b73b0bdd8493`
Run ID: `ledger-consensus-decoding-for-tool-agents-b73b0bdd8493-20260603T181440785957+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/788c4883ed21

## What looked useful

On 20,000 synthetic tasks per regime with 9 traces per task, ledger accuracy vs majority was 0.99760 vs 0.99345 for final-answer noise, 0.91200 vs 0.91450 for mixed trace noise, and 0.36170 vs 0.36050 for correlated wrong tool choice. A sample sweep showed large gains at 3 samples (+0.11417 and +0.12483 in the first two regimes) that mostly vanished by 9-15 samples.

## Boundaries and scale limits

No live LLMs, no real API tools, small arithmetic tool schema, CPU-only simulation, and no token/latency/cost measurement. Results should not be generalized to production tool agents without live-model trace benchmarks.

## Claim scope

Synthetic executable arithmetic tool-call traces show ledger consensus can improve low-sample accuracy when errors are externally checkable, but it provides little or no advantage over final-answer majority at 9 or more samples and does not detect correlated wrong-but-internally-verified tool choices.

## Why it stopped

Proxy simulation found a narrow mechanism benefit but not broad evidence for a paper-ready decoding method; ledger verification cannot distinguish correlated semantically wrong tool choices when their calls are internally executable.

## Recommended next action

Stop as no-paper useful signal; next bounded test should use live-model tool-call traces and compare ledger consensus against answer majority, trace majority, and verifier reranking at equal sample and token budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live-Model Ledger Consensus on Tool-Call Traces
- Success threshold: At 9 samples, ledger consensus improves accuracy by at least 3 percentage points over final-answer majority on live traces without more than a 1 percentage point regression in correlated semantic-error subsets, at comparable token budget.
- Stop condition: Stop if live traces show less than 1 percentage point accuracy gain over final-answer majority at 5 and 9 samples, or if gains occur only on toy parser errors absent from realistic traces.

## Evidence references

- Artifact root: `<local-path>/projects/ledger-consensus-decoding-for-tool-agents-b73b0bdd8493`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

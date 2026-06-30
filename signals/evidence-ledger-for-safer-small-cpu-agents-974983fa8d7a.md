# Evidence Ledger for Safer Small CPU Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-for-safer-small-cpu-agents-974983fa8d7a`
Run ID: `evidence-ledger-for-safer-small-cpu-agents-974983fa8d7a-20260602T121303614941+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/3c64525017c9

## What looked useful

Across the 50,000-episode main run, the unguarded baseline committed unsupported actions at 24.598%, while the ledger gate allowed 0 unsupported actions and false-blocked 2.91% of valid actions. Across five 20,000-episode seeds, mean baseline unsafe rate was 24.816%, mean ledger unsafe allow rate was 0%, and mean false-block rate was 3.048%.

## Boundaries and scale limits

No real LLM agent, real file edits, production tool APIs, human workflow, or non-ledger guardrail baseline was tested. Unsupported proposal frequency was parameterized in the synthetic planner.

## Claim scope

Synthetic CPU benchmark of a citation-validating evidence ledger for state-changing ticket updates. The ledger blocked unsupported target IDs introduced by prompt distractors while allowing cited current-workspace records.

## Why it stopped

No-paper useful signal: this run supports the scoped synthetic mechanism, but it is proxy evidence and not a full validation of real small CPU agents.

## Recommended next action

Run a bounded real-agent follow-up by integrating the ledger gate into a small local CPU agent on file/task workflows and comparing it with at least one non-ledger guardrail baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-agent evidence ledger guardrail benchmark
- Success threshold: Ledger unsafe action rate is at least 50% lower than the strongest non-ledger baseline, false block rate is below 10%, and task completion drops by less than 15% on at least 200 labeled real-agent episodes.
- Stop condition: Stop if the ledger does not beat the strongest non-ledger baseline on unsafe action rate, or if false blocks exceed 10% after one citation-repair pass.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-safer-small-cpu-agents-974983fa8d7a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

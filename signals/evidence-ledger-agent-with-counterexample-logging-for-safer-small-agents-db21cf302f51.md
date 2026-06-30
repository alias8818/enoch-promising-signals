# Evidence-Ledger Agent with Counterexample Logging for Safer Small Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-agent-with-counterexample-logging-for-safer-small-agents-db21cf302f51`
Run ID: `evidence-ledger-agent-with-counterexample-logging-for-safer-small-agents-db21cf302f51-20260621T220712206812+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/cf76d8b746b8

## What looked useful

Corrected 20-seed benchmark over 100,000 decisions per agent showed unsafe action rate falling from 0.3521 to 0.1329 at cex_k=2, mean utility improving from -0.4185 to 0.1078, and a monotonic unsafe-action improvement across cex_k 0, 1, 2, and 3.

## Boundaries and scale limits

Synthetic cases only; no real LLM, real retrieval corpus, real tool side effects, adversarial prompt set, or long-horizon memory persistence was tested.

## Claim scope

In a synthetic noisy-evidence benchmark, an evidence-ledger policy with targeted counterexample logging reduced unsafe actions versus a simple evidence-counting baseline, with little change in safe-case abstention.

## Why it stopped

No-paper closure: the current result is a synthetic mechanism signal, not direct publication-grade evidence for safer small agents.

## Recommended next action

Run a bounded direct evaluation around an actual small LLM/tool agent on naturalistic safety-graded tasks using the same unsafe-action, abstention, utility, and counterexample-depth metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct Small-LLM Tool-Agent Evidence-Ledger Evaluation
- Success threshold: At least 25% relative unsafe-action reduction with no more than a 5 percentage-point safe-abstention increase across at least 300 graded tasks and three random seeds.
- Stop condition: Stop if the ledger variant fails to reduce unsafe actions by at least 10% relative in an initial 100-task smoke evaluation or if trace inspection shows counterexamples are not causally influencing decisions.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-with-counterexample-logging-for-safer-small-agents-db21cf302f51`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

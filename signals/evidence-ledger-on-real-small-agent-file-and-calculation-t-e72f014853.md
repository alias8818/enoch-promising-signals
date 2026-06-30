# Evidence ledger on real small-agent file and calculation tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-on-real-small-agent-file-and-calculation-t-e72f014853`
Run ID: `evidence-ledger-on-real-small-agent-file-and-calculation-t-e72f014853-20260608T062141407320+0000`

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

- Parent run decision: Evidence ledger for small CPU agent reliability: enoch://control-plane/projects/evidence-ledger-for-small-cpu-agent-reliability-d2e6750b2b3a/runs/evidence-ledger-for-small-cpu-agent-reliability-d2e6750b2b3a-20260608T003135348502+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/4dc5f69bcaa8

## What looked useful

Across 1,000 cases per condition, baseline and record-only ledger accuracy were both 0.715, while verified ledger accuracy was 1.000 with zero false repairs in a 500-case no-slip control. The result supports ledger verification as a useful mechanism but not a paper-ready autonomous-agent claim.

## Boundaries and scale limits

The run used generated local files, deterministic injected slips, and task-specific verifiers. It did not test live LLM agents, broad real-world task distributions, adversarial files, or general-purpose verifier construction.

## Claim scope

In a controlled local benchmark of generated small file and calculation tasks, an evidence ledger with independent verification of file observations and arithmetic eliminated matched injected errors, while a record-only ledger did not improve accuracy.

## Why it stopped

Tier 1 direct mechanism test completed; evidence supports the mechanism in a controlled setting but is not paper-positive because model-agent behavior was proxied by injected slips and verifiers were task-specific.

## Recommended next action

Run a bounded live-agent follow-up using a small LLM on held-out file/calculation tasks, comparing baseline, record-only ledger, verified ledger, and verifier-only controls with latency and false-rejection metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live small-LLM evidence-ledger test on file and calculation tasks
- Success threshold: Verified ledger improves accepted-answer accuracy by at least 15 percentage points over both baseline and record-only ledger, with false rejection or false repair below 5% and median latency overhead below 2x on the bounded task set.
- Stop condition: Stop if verified ledger fails to improve accuracy by at least 5 percentage points, if false repairs exceed 10%, or if median latency overhead exceeds 3x without a compensating accuracy gain.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-on-real-small-agent-file-and-calculation-t-e72f014853`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

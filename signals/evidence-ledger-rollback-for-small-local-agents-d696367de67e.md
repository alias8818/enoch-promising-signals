# Evidence-ledger rollback for small local agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-rollback-for-small-local-agents-d696367de67e`
Run ID: `evidence-ledger-rollback-for-small-local-agents-d696367de67e-20260604T161240901624+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/787b7ccf8e16

## What looked useful

Main run: naive success 0.3074, full recompute success 0.9686 at 393.28 mean cost units, ledger rollback success 0.9584 at 193.85 mean cost units. Rollback replay updates averaged 4.10 versus 203.58 for full recompute.

## Boundaries and scale limits

Proxy-only evidence; no live LLM agent, natural-language evidence extraction, real verifier, filesystem/API side effects, or long-horizon multi-agent workload was tested. Main run used 5000 synthetic tasks per policy and sensitivity sweeps used 2000 tasks per setting.

## Claim scope

In a deterministic synthetic small-agent state simulator with noisy evidence, oracle-known task facts, parameterized verifier detection, and cheap perfect checkpoints, evidence-ledger rollback recovered from detected false evidence with success close to full recompute while preserving near-naive cost.

## Why it stopped

Closed as no-paper useful signal because the mechanism is supported only by synthetic proxy evidence, not direct real-agent validation.

## Recommended next action

Run a bounded real-agent follow-up with a small local model/tool harness on 100 to 300 seeded file/QA/debug tasks, comparing no-rollback, full recompute, and evidence-ledger rollback on task success and replay/token/wall-clock cost.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real local-agent evidence-ledger rollback benchmark
- Success threshold: Rollback success is within 5 percentage points of full recompute and at least 20 percentage points above no-rollback while reducing replay tokens/actions by at least 50% versus full recompute.
- Stop condition: Stop as negative if rollback is more than 5 percentage points below full recompute success or fails to reduce replay tokens/actions by at least 50% on the seeded benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-rollback-for-small-local-agents-d696367de67e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

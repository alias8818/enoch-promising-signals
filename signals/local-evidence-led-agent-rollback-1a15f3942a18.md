# Local Evidence-Led Agent Rollback

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `local-evidence-led-agent-rollback-1a15f3942a18`
Run ID: `local-evidence-led-agent-rollback-1a15f3942a18-20260604T184132922686+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/3c542971de2e

## What looked useful

Evidence-led rollback reduced some hidden breakage but discarded useful progress and amplified noisy local evidence; main run mean final score was 0.282995 for evidence_led versus 0.30958 for no rollback, with bootstrap delta -0.02654 and 95% CI [-0.03582, -0.01714].

## Boundaries and scale limits

This is a local CPU-only simulation, not a real LLM coding-agent benchmark. It does not validate behavior on real repositories, real unit tests, long-horizon tool use, or model-driven edit distributions.

## Claim scope

In a synthetic sequential-edit agent model with noisy partial local evidence, hidden requirements, and rollback cost, the tested evidence-led rollback policy did not improve latent final quality over no rollback and was statistically indistinguishable from a simpler recent-passing rollback baseline.

## Why it stopped

Proxy evidence does not support the broad local evidence-led rollback hypothesis and is not paper-ready; the result is an early simulation falsification rather than full validation.

## Recommended next action

Stop this proxy run as an early falsification; only reopen with a bounded real-agent benchmark that measures hidden-test pass rate and progress lost under identical rollback policies.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Agent Rollback Benchmark With Hidden Tests
- Success threshold: Evidence-led rollback must improve hidden-test pass rate or latent final task score over both no rollback and recent-passing rollback, with 95% paired/bootstrap intervals excluding zero, while adding less than 25% wall-clock overhead.
- Stop condition: Stop if evidence-led rollback is not better than no rollback or recent-passing rollback on hidden-test pass rate after the first 30 tasks, or if overhead exceeds 25% without a compensating quality gain.

## Evidence references

- Artifact root: `<local-path>/projects/local-evidence-led-agent-rollback-1a15f3942a18`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# Evidence Ledger for Tiny CPU-Bound Agent Tool Use

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-for-tiny-cpu-bound-agent-tool-use-5b0c915db57b`
Run ID: `evidence-ledger-for-tiny-cpu-bound-agent-tool-use-5b0c915db57b-20260601T094020886206+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/267e7cf44e81

## What looked useful

A ledger layered on a weak prior achieved 0.83415 mean success versus 0.8702 for the weak-prior baseline, while reducing CPU units/task from 10.6434 to 9.26535. The paired success delta was -0.03605 with approximate 95% CI [-0.04030, -0.03180], indicating a cost/success tradeoff rather than a quality improvement.

## Boundaries and scale limits

Synthetic controller-only workload; no real LLM, real tool APIs, production traces, or long-horizon persistent sessions were tested. Benchmark used 40 seeds, 500 tasks per seed, 3-call budget, single CPU process.

## Claim scope

On a synthetic repeated tool-use benchmark for tiny CPU-bound controllers, evidence-ledger variants reduced CPU cost and wall time but did not improve success rate over a reasonable weak-prior non-ledger baseline.

## Why it stopped

Proxy/controller benchmark early-falsified the primary success-improvement claim; evidence-ledger variants improved CPU cost but lost success against the relevant weak-prior baseline, so this is not a full validation or paper-ready positive result.

## Recommended next action

Stop this run as a no-paper useful signal; only continue with a bounded utility-optimized ledger test that requires maintaining weak-prior success within 1 percentage point while reducing CPU cost by at least 10%.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Utility-Optimized Evidence Ledger for Tiny Tool Selection
- Success threshold: Mean success no more than 0.01 below weak_prior and mean CPU units at least 10% lower than weak_prior, with paired 95% confidence intervals excluding weaker tradeoffs.
- Stop condition: Stop if no parameter setting meets both the success-retention and CPU-reduction thresholds on 40 matched seeds, or if gains only appear after tuning on the evaluation seeds.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-tiny-cpu-bound-agent-tool-use-5b0c915db57b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

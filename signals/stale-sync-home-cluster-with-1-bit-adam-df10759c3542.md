# Stale-sync home cluster with 1-bit Adam

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `stale-sync-home-cluster-with-1-bit-adam-df10759c3542`
Run ID: `stale-sync-home-cluster-with-1-bit-adam-df10759c3542-20260525T114541011239+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/625d0a40f048

## What looked useful

The mechanism did not collapse in a bounded proxy: 1-bit stale sync matched full-precision stale sync closely on accuracy while sharply reducing worker upload traffic. Error feedback was not materially better than no-error-feedback in this small setting.

## Boundaries and scale limits

Not a real home cluster, not a networked wall-clock benchmark, not large-model training, not GPT-2-small-class evidence, and still assumes full-precision downlink broadcasts.

## Claim scope

In a single-host synthetic 4-worker non-IID classification proxy, stale/local Adam with 1-bit sign-delta synchronization preserved mean test accuracy within about 0.5-0.9 percentage points of synchronous Adam while reducing upload communication by about 126x at sync interval 4 and about 503x at sync interval 16.

## Why it stopped

Closed as no-paper useful signal because the evidence is a synthetic proxy and does not directly validate real home-cluster networking or language-model training.

## Recommended next action

Run a bounded direct follow-up using multi-process or multi-node throttled networking on a small transformer/GPT-2-small-class workload, measuring validation quality and wall-clock throughput against synchronous Adam and full-precision local Adam.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Throttled multi-process transformer test for stale 1-bit Adam sync
- Success threshold: 1-bit stale/local Adam is within 2% relative validation loss or perplexity of full-precision local Adam and improves constrained-network wall-clock throughput by at least 20% at the same training budget.
- Stop condition: Stop if 1-bit stale/local Adam is more than 5% worse in validation loss or perplexity than full-precision local Adam after matched budget, or if communication savings do not translate into at least 10% measured throughput improvement under throttling.

## Evidence references

- Artifact root: `<local-path>/projects/stale-sync-home-cluster-with-1-bit-adam-df10759c3542`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

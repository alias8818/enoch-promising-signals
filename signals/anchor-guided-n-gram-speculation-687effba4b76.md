# Anchor-Guided N-Gram Speculation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-guided-n-gram-speculation-687effba4b76`
Run ID: `anchor-guided-n-gram-speculation-687effba4b76-20260604T145136670455+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/c108e0d23655

## What looked useful

Anchor gating consistently raised acceptance rate, by 17.1%-56.2% on the synthetic corpus and 30.6%-276.4% on Tiny Shakespeare, while consistently reducing the speed proxy by 3.3%-10.7% and 1.1%-7.6% respectively because draft coverage collapsed.

## Boundaries and scale limits

This was a CPU-only simulator with exact held-out-token verification, n-gram orders 2-4, draft lengths 2-6, one synthetic corpus, and a 200k-token Tiny Shakespeare slice. It did not measure real target-model GPU throughput, KV-cache costs, batching, stochastic decoding quality, or large-corpus robustness.

## Claim scope

In a bounded n-gram speculative decoding simulator over synthetic anchor-heavy text and Tiny Shakespeare, confidence/anchor-gated n-gram drafting improved acceptance precision and reduced wasted draft tokens but did not improve accepted tokens per target verification step over always-on n-gram drafting.

## Why it stopped

Proxy/early falsification: anchor-only gating improved draft precision but lost to always-on n-gram speculation on the target-step speed proxy in every matched setting tested; this is not a full serving validation.

## Recommended next action

Stop this run as no-paper useful signal; the concrete next bounded test is an adaptive policy that keeps always-on short drafts but uses anchors only to extend draft length when confidence is high.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive anchor-extended n-gram speculation
- Success threshold: Adaptive anchor-extended drafting improves speedup_proxy by at least 5% over the best always-on fixed-length n-gram baseline on both datasets while not increasing waste_per_accepted by more than 10%.
- Stop condition: Stop if adaptive policy fails to beat the best always-on speedup_proxy on either dataset or if gains appear only by reducing draft coverage below 50% of the always-on baseline.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-guided-n-gram-speculation-687effba4b76`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

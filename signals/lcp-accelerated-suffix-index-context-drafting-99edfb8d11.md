# LCP-accelerated suffix-index context drafting

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `lcp-accelerated-suffix-index-context-drafting-99edfb8d11`
Run ID: `lcp-accelerated-suffix-index-context-drafting-99edfb8d11-20260524T050011598399+0000`

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

- Parent run decision: Rolling suffix-array context drafting: enoch://control-plane/projects/rolling-suffix-array-context-drafting-c1bed41f798b/runs/rolling-suffix-array-context-drafting-c1bed41f798b-20260524T044733896526+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9b19fa4a73f3

## What looked useful

Suffix-index drafting recovered long repeated continuations in the high-reuse setting at 6.792 accepted tokens per 8-token draft and produced zero accepted tokens on the random control, but it only reached 1.34x the 2-gram baseline and LCP expansion showed 5.215x estimated range-work reduction rather than the required 10x.

## Boundaries and scale limits

No real language model, no speculative decoding integration, no real corpus, no GPU serving measurement, and no paper-scale robustness sweep. Full run used at most 720 queries per repeated scenario and about 60k training tokens.

## Claim scope

Controlled small direct token-stream test of exact-match suffix-index context drafting with LCP occurrence-range recovery on synthetic repeated-context and random-control streams.

## Why it stopped

Tier 1 controlled direct test failed the pre-registered 2x accepted-token improvement and 10x LCP work-reduction thresholds, though it did support the basic repeated-context mechanism.

## Recommended next action

Stop this run as no-paper useful signal; a separate bounded follow-up should test the drafter on a real repeated-context corpus with stronger short-context and retrieval baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus suffix-index drafting with strong retrieval baselines
- Success threshold: Suffix-index drafting achieves at least 2x accepted tokens per query over the best baseline on the real corpus, LCP/RMQ range recovery is draft-identical to plain expansion, and occurrence-range work drops by at least 10x without failing the negative control.
- Stop condition: Stop if suffix-index accepted tokens are below 1.5x the best baseline, if LCP/RMQ does not reproduce plain drafts, or if the negative control shows nonzero meaningful accepted continuations.

## Evidence references

- Artifact root: `<local-path>/projects/lcp-accelerated-suffix-index-context-drafting-99edfb8d11`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

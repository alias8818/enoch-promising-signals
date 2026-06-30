# Controlled prompt-suite comparison for GPT-2 n-gram draft sources

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `controlled-prompt-suite-comparison-for-gpt-2-n-gram-draft-db1e32f95a`
Run ID: `controlled-prompt-suite-comparison-for-gpt-2-n-gram-draft-db1e32f95a-20260603T145002972569+0000`

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

- Parent run decision: N-gram speculative draft for local GPT-2 inference: enoch://control-plane/projects/n-gram-speculative-draft-for-local-gpt-2-inference-f3eda082a24c/runs/n-gram-speculative-draft-for-local-gpt-2-inference-f3eda082a24c-20260602T195822719118+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/b6e6e6737050

## What looked useful

Across five seeds, in-domain n-gram draft sources beat shuffled controls by mean acceptance-probability delta 0.3176, with positive deltas in 5/5 seeds and every suite. However, in-domain sources did not consistently beat pooled or best cross-domain sources, so the result supports a structured-source mechanism but not the stronger prompt-suite matching claim.

## Boundaries and scale limits

The evidence uses tiny hand-authored prompt suites, GPT-2-small only, token-level proposal scoring, and no end-to-end speculative decoding throughput measurement. It does not show publication-grade robustness or consistent in-domain superiority over pooled/best cross-domain draft sources.

## Claim scope

In a small controlled GPT-2-small test with four hand-authored prompt suites, structured suite-specific 4-gram draft sources produced higher GPT-2 speculative-style acceptance probabilities than a shuffled-token n-gram control across all suites and five seeds.

## Why it stopped

Tier 1 direct GPT-2-small evidence produced a useful mechanism signal but not a paper-ready or robust in-domain superiority result.

## Recommended next action

Run a bounded deepen follow-up with larger real prompt-suite corpora and end-to-end speculative decoding throughput/acceptance curves while retaining shuffled, pooled, and cross-domain controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Larger prompt-suite n-gram draft sources for GPT-2 speculative decoding
- Success threshold: Suite-matched draft sources improve mean acceptance probability by at least 0.10 over shuffled controls and at least 0.03 over pooled/best cross-domain controls in at least 3 of 4 suites, with a measured end-to-end decoding speedup over greedy GPT-2.
- Stop condition: Stop if suite-matched sources fail to beat pooled/best cross-domain controls by 0.03 in at least 3 of 4 suites or if token acceptance improvements do not translate into any end-to-end throughput gain.

## Evidence references

- Artifact root: `<local-path>/projects/controlled-prompt-suite-comparison-for-gpt-2-n-gram-draft-db1e32f95a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

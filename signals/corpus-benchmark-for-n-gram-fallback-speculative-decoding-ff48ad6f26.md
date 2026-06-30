# Corpus benchmark for n-gram fallback speculative decoding

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `corpus-benchmark-for-n-gram-fallback-speculative-decoding-ff48ad6f26`
Run ID: `corpus-benchmark-for-n-gram-fallback-speculative-decoding-ff48ad6f26-20260608T082835229100+0000`

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

- Parent run decision: Spec-Decoding with N-gram Fallback: enoch://control-plane/projects/spec-decoding-with-n-gram-fallback-6bfdcae87d4c/runs/spec-decoding-with-n-gram-fallback-6bfdcae87d4c-20260607T230436323963+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/fec5ab3734c4

## What looked useful

The mechanism cleared the Tier 1 direct corpus threshold: all three GPT-2 BPE corpora exceeded 1.10 mean advance per target call, with 13.91%-19.74% simulated call reduction and shuffled controls near no-draft. This is useful no-paper evidence for trying a real LM-serving implementation.

## Boundaries and scale limits

No actual target language model, draft fallback integration, serving stack, GPU timing, memory overhead, prompt diversity benchmark, or multi-corpus large-scale validation was run. The corpus-prefix setup mainly represents document-continuation/cache reuse scenarios.

## Claim scope

Offline held-out corpus replay on three small public text corpora shows that a prefix-trained n-gram fallback can improve simulated speculative verification efficiency for GPT-2 BPE tokens. Best practical n=2, max_draft=8 rows achieved 1.1615-1.2459 held-out tokens advanced per target verification call, versus matched shuffled-train controls at 1.0038-1.0099.

## Why it stopped

Tier 1 direct corpus evidence supports the mechanism but is not a full validation or paper-ready serving result.

## Recommended next action

Implement the n-gram fallback inside a small real speculative decoding loop for a GPT-2-small-class or similar local target model and measure acceptance, wall-clock latency, memory overhead, and quality neutrality on document-continuation prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model latency benchmark for n-gram fallback speculative decoding
- Success threshold: On at least 100 document-continuation prompts and at least 10,000 generated BPE tokens, show at least 10% wall-clock tokens/sec improvement over no-draft decoding with no output changes under deterministic decoding and memory overhead below 10% of target-model memory.
- Stop condition: Stop if integrated fallback overhead makes tokens/sec improvement under 5%, if acceptance-derived target-call reduction falls below 1.05x, or if deterministic outputs diverge from the no-draft target path.

## Evidence references

- Artifact root: `<local-path>/projects/corpus-benchmark-for-n-gram-fallback-speculative-decoding-ff48ad6f26`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

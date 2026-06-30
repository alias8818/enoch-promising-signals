# Suffix-tree n-gram draft for speculative decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-n-gram-draft-for-speculative-decoding-9f8058099b1e`
Run ID: `suffix-tree-n-gram-draft-for-speculative-decoding-9f8058099b1e-20260530T072451025092+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/561ff17d42d8

## What looked useful

Suffix n-gram improved GPT-2 greedy mean accepted tokens per 4-token draft from 0.1732 for fixed 2-gram to 0.2350 across 1536 pooled prompts; paired bootstrap 95% CI for the lift was [0.0417, 0.0833]. The mechanism lift is reproducible but too small in absolute terms to support a paper or deployment speedup claim.

## Boundaries and scale limits

Three 512-prompt seeds, GPT-2-small greedy verifier only, Wikitext-2 only, draft length 4, max suffix context 12, acceptance proxy rather than optimized end-to-end speculative decoding wall-clock. No larger models, sampling verifier, code/log domains, or serving-load measurements were tested.

## Claim scope

On Wikitext-2 prompts with a GPT-2-small greedy verifier, an offline variable-order suffix n-gram drafter built from 80k training tokens accepted more draft tokens than unigram/fixed n-gram baselines, but absolute acceptance remained low.

## Why it stopped

Bounded direct verifier evidence supports only a small acceptance improvement and does not demonstrate practical end-to-end speedup; this is a proxy/medium confirmation, not full validation.

## Recommended next action

Stop this run as no-paper useful signal; run one bounded deepen test that integrates the suffix n-gram drafter into an actual speculative decoding loop on a repetition-heavy code or document-retrieval trace and measures wall-clock latency versus greedy decoding and fixed 2-gram drafting.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end suffix n-gram speculative decoding latency on repetition-heavy traces
- Success threshold: At least 5% end-to-end wall-clock tokens/sec improvement over greedy decoding and at least 3% improvement over fixed 2-gram drafting, with no worse than 5% p95 latency regression, on a bounded repetition-heavy trace.
- Stop condition: Stop as negative if first-token acceptance remains below 30% or measured end-to-end tokens/sec does not beat greedy decoding after controlling for verifier batch/window length and drafter overhead.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-n-gram-draft-for-speculative-decoding-9f8058099b1e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

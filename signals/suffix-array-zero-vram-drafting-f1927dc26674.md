# Suffix-Array Zero-VRAM Drafting

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `suffix-array-zero-vram-drafting-f1927dc26674`
Run ID: `suffix-array-zero-vram-drafting-f1927dc26674-20260523T054934770613+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/1d80b374474e

## What looked useful

A CPU suffix index is cheap to build and query, but accepted only about 0.27 tokens per 8-token draft with median 0 and no full 8-token suffix drafts accepted. Even the held-out true corpus continuation averaged only about 0.53-0.55 accepted tokens, indicating model-continuation mismatch is the main bottleneck.

## Boundaries and scale limits

Tested one public small corpus, one small target model, greedy generation, up to 256 held-out prompts, 8-token drafts, and suffix keys up to 16 tokens. Full speculative verifier wall-clock speedup, larger models, production traces, and target-shaped caches were not tested.

## Claim scope

Bounded early falsification for generic CPU/RAM lexical suffix-index drafting over Tiny Shakespeare against greedy distilgpt2 continuations: the drafter is zero-VRAM beyond the target model, but target-token acceptance is too low for practical speculative decoding.

## Why it stopped

Proxy/early falsification, not full validation: direct accepted-prefix tests against distilgpt2 show generic raw-corpus suffix drafts rarely match the target model, so a full serving benchmark is not justified from this evidence.

## Recommended next action

Stop this generic suffix-array drafting line as no-paper evidence; only pursue a bounded follow-up that indexes target-generated or previously accepted continuations rather than raw corpus text.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Target-Shaped Zero-VRAM Retrieval Draft Cache
- Success threshold: Mean accepted length >= 1.0 per 8-token draft, nonzero acceptance rate >= 50%, and estimated net speedup > 1.1x after CPU lookup overhead on at least 256 held-out prompts.
- Stop condition: Stop if target-shaped cache acceptance remains below 0.75 mean accepted tokens per 8-token draft or CPU lookup overhead erases estimated verifier savings.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-array-zero-vram-drafting-f1927dc26674`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

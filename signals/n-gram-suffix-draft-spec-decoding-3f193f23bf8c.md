# N-Gram Suffix Draft Spec Decoding

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `n-gram-suffix-draft-spec-decoding-3f193f23bf8c`
Run ID: `n-gram-suffix-draft-spec-decoding-3f193f23bf8c-20260621T172252384092+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/432efccc8092

## What looked useful

Naive suffix n-gram drafts occasionally match held-out continuations, but the best tested configuration averaged only 0.178 GPT-2 greedy-accepted draft tokens per context and an idealized 1.178x target-call speedup proxy before overhead. Higher-quality longer suffixes had very low coverage, and higher-coverage short suffixes had very low median target probability on drafted tokens.

## Boundaries and scale limits

No end-to-end speculative decoding runtime was implemented; no larger models, larger corpora, domain-specific caches, probabilistic draft distributions, or distribution-preserving speculative sampling were tested.

## Claim scope

Bounded local probe of deterministic suffix n-gram draft proposals built from WikiText-2 train text and verified against WikiText-2 validation contexts with GPT-2-small greedy next-token predictions.

## Why it stopped

Proxy/local evidence does not support the practical speedup hypothesis for naive corpus-level suffix n-gram drafts; this is an early bounded falsification, not a full validation across models or domains.

## Recommended next action

Stop this proxy run as no-paper evidence; a follow-up should implement end-to-end greedy speculative verification and require measured wall-clock speedup over target-only decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end greedy verification for suffix n-gram drafts
- Success threshold: At least 1.10x measured median tokens/second over target-only greedy decoding with identical greedy outputs on the repetition-heavy domain and no more than 5 percent slowdown on general text.
- Stop condition: Stop if optimized end-to-end decoding is below 1.05x median speedup on the repetition-heavy domain or slows general text by more than 5 percent.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-suffix-draft-spec-decoding-3f193f23bf8c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

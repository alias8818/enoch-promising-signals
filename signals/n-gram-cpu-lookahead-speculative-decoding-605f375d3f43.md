# N-gram CPU lookahead speculative decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-cpu-lookahead-speculative-decoding-605f375d3f43`
Run ID: `n-gram-cpu-lookahead-speculative-decoding-605f375d3f43-20260605T014744132524+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/08462091ff1f

## What looked useful

Short n-gram drafts are worth testing when the stream has repetition: Tiny Shakespeare reached 2.0477 proxy tokens per target call at n=4,k=4, periodic text reached 5.0, bursty text reached 3.3054, and random text reached only 1.0108. Longer drafts showed diminishing returns and much lower accepted/proposed ratios.

## Boundaries and scale limits

No real LM verifier, no BPE/sentencepiece tokenizer, no GPU overlap measurement, no quality-equivalence check, and only 256 KB bounded corpora plus partial 512 KB Tiny Shakespeare data.

## Claim scope

In a byte-token teacher-forced proxy over 256 KB corpora, an online CPU n-gram lookahead drafter reduces target verification calls on repetitive, bursty, and small natural-language streams, but provides essentially no benefit on random streams.

## Why it stopped

The run produced a bounded proxy signal but not direct model-acceptance or serving-speed evidence, so it should not be treated as publication-grade validation.

## Recommended next action

Stop this worker run as no-paper useful-signal evidence; the next bounded step is a direct LM verifier experiment with the same online n-gram drafter on BPE tokens and wall-clock speed measurement.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct LM acceptance test for online n-gram speculative lookahead
- Success threshold: At least 20% wall-clock tokens/sec improvement on repetition-heavy prompts with exact greedy-output parity, while natural/random controls do not regress by more than 5%.
- Stop condition: Stop if accepted draft tokens average below 0.25 per verifier call on natural and repetitive prompt classes, or if CPU drafting overhead eliminates verifier-call savings.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-cpu-lookahead-speculative-decoding-605f375d3f43`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# N-Gram Suffix Draft for Tiny Model Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-suffix-draft-for-tiny-model-speculative-decoding-fc17bfb00740`
Run ID: `n-gram-suffix-draft-for-tiny-model-speculative-decoding-fc17bfb00740-20260524T171258541669+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/43764c537a02

## What looked useful

Suffix n-gram lookup is negligible-cost and consistently improved simulated verifier-cycle count over cheap controls on GPT-2/WikiText-2, but accepted-token rates were low: 8.73% at draft length 2, 4.66% at draft length 4, 2.41% at draft length 8, and 1.29% at draft length 16.

## Boundaries and scale limits

This run used 48 prompts, 3072 generated GPT-2 target tokens, a 120k-token WikiText-2 suffix memory, greedy decoding only, and trace-level verifier-cycle simulation. It did not implement end-to-end speculative decoding wall-clock measurement, sampling, batched serving, chat/instruction models, or an actual tiny neural draft model.

## Claim scope

On a bounded GPT-2-small/WikiText-2 greedy-continuation trace, a static suffix n-gram drafter reduced simulated speculative verifier cycles by 10.25% to 13.93% versus one target step per token and beat unigram and repeat-tail controls.

## Why it stopped

The result supports the mechanism only as a bounded trace-level proxy; low acceptance rates and missing end-to-end wall-clock validation make it insufficient for a paper-positive decision.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should implement real end-to-end speculative decoding wall-clock measurement with prompt-local and corpus-local suffix caches versus a neural draft baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-End Prompt-Local Suffix Cache for GPT-2 Speculative Decoding
- Success threshold: At least 8% end-to-end tokens/s improvement over no-draft GPT-2 greedy decoding on 1000 or more generated tokens with identical greedy outputs and no regression versus repeat-tail control.
- Stop condition: Stop if suffix-cache variants fail to exceed repeat-tail control by 3 percentage points in end-to-end tokens/s or if verifier overhead eliminates the simulated cycle-reduction benefit.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-suffix-draft-for-tiny-model-speculative-decoding-fc17bfb00740`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

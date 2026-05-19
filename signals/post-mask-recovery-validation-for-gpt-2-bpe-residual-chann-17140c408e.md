# Post-mask recovery validation for GPT-2 BPE residual-channel preservation

Status: `useful_signal`
Project ID: `post-mask-recovery-validation-for-gpt-2-bpe-residual-chann-17140c408e`
Run ID: `post-mask-recovery-validation-for-gpt-2-bpe-residual-chann-17140c408e-20260516T211012717801+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Post-mask recovery validation for GPT-2 BPE residual-channel preservation: internal_generated:post-mask-recovery-validation-for-gpt-2-bpe-residual-chann-17140c408e

## What looked useful

First-BPE masking yielded 58.0% top-1 and 78.9% top-5 word recovery versus 0.0% top-1 and 0.1% top-5 for whole-word masking, but equal-known-character controls matched or exceeded it, with random known characters reaching 73.2% top-1.

## Boundaries and scale limits

3,711 WikiText-2 validation/test multi-token word instances; tokenizer-level dictionary recovery only; no transformer hidden-state recovery, no neural adversary, no non-English corpus, and no alternate tokenizer family replication.

## Claim scope

On WikiText-2 multi-token words under GPT-2 BPE, post-tokenization partial masks leave residual substrings that permit high dictionary recovery, but the effect is explained by revealed characters rather than a distinctive GPT-2 BPE mechanism.

## Why it stopped

Bounded direct tokenizer-level validation found a real recovery signal but controls falsified the stronger paper-readiness interpretation; follow-up depth is already 4, so no further deepen/retry follow-up is recommended.

## Recommended next action

Stop this follow-up campaign at depth 4; preserve the result as no-paper evidence that post-BPE partial masking leaks substrings, but not as evidence for a distinctive GPT-2 BPE residual-channel mechanism.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/post-mask-recovery-validation-for-gpt-2-bpe-residual-chann-17140c408e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

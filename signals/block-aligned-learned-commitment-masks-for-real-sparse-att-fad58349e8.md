# Block-Aligned Learned Commitment Masks for Real Sparse Attention Speedup

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `58`
Project ID: `block-aligned-learned-commitment-masks-for-real-sparse-att-fad58349e8`
Run ID: `block-aligned-learned-commitment-masks-for-real-sparse-att-fad58349e8-20260518T075207099879+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `58`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Block-Aligned Learned Commitment Masks for Real Sparse Attention Speedup: internal_generated:block-aligned-learned-commitment-masks-for-real-sparse-att-fad58349e8

## What looked useful

The mechanism is plausible: trained low-rank selectors reached about 0.87-0.91 oracle block recall on held-out synthetic seeds and produced 1.81x-3.80x end-to-end speedups at 4096-8192 tokens with low mean output error versus dense attention. However, the real GPT-2 activation check at 1024 tokens was not end-to-end positive for learned masks.

## Boundaries and scale limits

No end-to-end transformer integration, no language-model loss/task-quality evaluation, no backward/training validation, no multi-model or multi-layer robustness, no optimized library baseline beyond PyTorch SDPA, and real GPT-2 activation evidence is limited to one 1024-token layer.

## Claim scope

On a local NVIDIA GB10, a custom Triton forward block-sparse attention kernel with block-aligned committed masks can beat PyTorch dense SDPA for fixed and learned masks on structured synthetic QKV at 4096-8192 tokens; a one-layer GPT-2 activation sanity check at 1024 tokens shows sparse-kernel speedups for oracle masks but not learned-mask end-to-end speedups once selector overhead is included.

## Why it stopped

No-paper closure: evidence supports a bounded mechanism signal, but Tier-4 paper-readiness is not met because learned-mask speedups are mainly synthetic and lack end-to-end language-model quality validation.

## Recommended next action

Stop this follow-up at depth 4; preserve the useful kernel/selector evidence but do not write a paper without an end-to-end transformer quality and throughput validation.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/block-aligned-learned-commitment-masks-for-real-sparse-att-fad58349e8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

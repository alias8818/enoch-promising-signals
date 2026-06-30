# Direct Small-Model Speculative Decoding Test for Anchor-Seeded Drafting

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `direct-small-model-speculative-decoding-test-for-anchor-se-9708982d29`
Run ID: `direct-small-model-speculative-decoding-test-for-anchor-se-9708982d29-20260610T145125358673+0000`

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

- Parent run decision: Anchor-Seeded Drafting for Speculative Decoding on Code and Text: enoch://control-plane/projects/anchor-seeded-drafting-for-speculative-decoding-on-code-and-text-2b948508ed6b/runs/anchor-seeded-drafting-for-speculative-decoding-on-code-and-text-2b948508ed6b-20260610T103258416720+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b3efcd0e635c

## What looked useful

Anchor seeding raised accepted proposal rate from 0.5247 to 0.6872 and a free-oracle anchor improved emitted tokens per counted target call by about 19-20% across block sizes. The charged anchor variant reduced emitted tokens per target call by about 40% across block sizes, failing the practical success threshold.

## Boundaries and scale limits

Small prompt set, GPT-2-family models only, greedy decoding only, no production KV-cache scheduler, and no larger target/draft model pairs. The free-oracle anchor result is a mechanism diagnostic rather than deployable evidence.

## Claim scope

On a Tier 1 direct small-model greedy speculative decoding test using gpt2 as target, distilgpt2 as draft, 16 prompts, 48 generated tokens per prompt, and block sizes 2/4/8, a target-derived block-start anchor improves proposal acceptance but does not improve practical target-call yield when the extra anchor target call is charged.

## Why it stopped

Tier 1 direct evidence supports the acceptance mechanism but falsifies the naive charged anchor-seeding threshold; this is not a full validation or paper-positive result.

## Recommended next action

Stop this run as no-paper useful evidence; the concrete next bounded test is to evaluate whether anchors can be recycled from verification/KV-cache state without an extra serial target call.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cached or Recycled Anchor Source for Speculative Drafting
- Success threshold: The cached/recycled-anchor variant must improve emitted tokens per target call by at least 10% over vanilla and preserve exact target-greedy output on all tested prompts.
- Stop condition: Stop if the variant needs an extra serial target call per block or if emitted tokens per target call is not at least 10% above vanilla on the gpt2/distilgpt2 controlled test.

## Evidence references

- Artifact root: `<local-path>/projects/direct-small-model-speculative-decoding-test-for-anchor-se-9708982d29`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

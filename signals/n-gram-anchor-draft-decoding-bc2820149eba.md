# N-Gram Anchor Draft Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-anchor-draft-decoding-bc2820149eba`
Run ID: `n-gram-anchor-draft-decoding-bc2820149eba-20260524T064522877201+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/20590bd957c4

## What looked useful

Long n-gram anchors are precise but sparse: Pride n=3..8 had 13.5% eligibility and 2.91 accepted corpus tokens per eligible proposal, while Moby n=3..8 had 8.75% eligibility and 0.63 accepted tokens per eligible proposal. Bigram relaxation increased coverage but did not consistently beat simpler baselines per position.

## Boundaries and scale limits

Local CPU-only probe; two natural-language corpora; 8-token drafts; 512-token recent context; small distilgpt2 target-greedy sanity checks only; no end-to-end speculative decoding wall-clock benchmark.

## Claim scope

On two public-domain natural-language books with 400 sampled positions each, n-gram anchor drafting finds high-quality continuations when repeated anchors exist, but low eligibility prevents robust accepted-token-per-position gains over simple unigram or repeat-last controls.

## Why it stopped

Bounded local evidence is mixed and no-paper: the mechanism is real when anchors fire, but coverage and corpus dependence prevent a robust standalone decoding result.

## Recommended next action

Stop this standalone claim; run one bounded follow-up that tests a gated n-gram-anchor add-on inside actual speculative decoding on repetition-heavy code/log/RAG corpora against unigram and no-draft controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Gated N-Gram Anchors for Repetition-Heavy Speculative Decoding
- Success threshold: At least 10% wall-clock tokens/sec improvement over the best simple copy baseline on two repetition-heavy domains, with no regression greater than 3% on prose control.
- Stop condition: Stop if n-gram anchors add less than 3% wall-clock speedup over unigram/repeat controls on both repetition-heavy domains or if verification overhead erases accepted-token gains.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-anchor-draft-decoding-bc2820149eba`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

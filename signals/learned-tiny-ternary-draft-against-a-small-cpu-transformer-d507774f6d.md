# Learned Tiny Ternary Draft Against a Small CPU Transformer

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `learned-tiny-ternary-draft-against-a-small-cpu-transformer-d507774f6d`
Run ID: `learned-tiny-ternary-draft-against-a-small-cpu-transformer-d507774f6d-20260608T102755668748+0000`

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

- Parent run decision: Tiny Ternary Draft for CPU Spec-Decode: enoch://control-plane/projects/tiny-ternary-draft-for-cpu-spec-decode-d09308f38756/runs/tiny-ternary-draft-for-cpu-spec-decode-d09308f38756-20260608T045912183312+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/4244dd767c13

## What looked useful

Ternary quantization retained 91.9% of the dense draft top-1 agreement and put the target top-1 token in its top-8 candidates on 64.0% of strict held-out contexts, but ternary top-1 agreement was 29.8%, below the memorized last-token control at 31.6% and therefore failed the primary success threshold.

## Boundaries and scale limits

No full speculative-decoding verifier loop, no broad benchmark corpus, no larger target model, and no end-to-end serving speedup measurement. The main held-out split is small and local, though it uses a real 81.9M-parameter CPU transformer target.

## Claim scope

Tier 1 CPU-only direct test of a learned hashed-context ternary draft against distilgpt2 top-1 next-token labels on 228 held-out local technical-prose contexts after candidate-vocabulary coverage filtering.

## Why it stopped

Controlled Tier 1 direct test produced mixed evidence and failed the primary top-1 control threshold; this is not a full validation or paper-ready result.

## Recommended next action

Stop this run as a no-paper useful signal; a bounded next test should implement probability-based speculative verification and train a stronger ternary draft that must beat last-token and n-gram controls on held-out prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Probability-Based Ternary Draft Verification Against distilgpt2
- Success threshold: On at least 500 held-out contexts, ternary draft top-1 agreement must exceed the best cheap control by >=5 absolute percentage points, retain >=80% of dense draft agreement, and produce a measured end-to-end CPU decoding speedup over target-only greedy decoding.
- Stop condition: Stop if the ternary draft again fails to beat the best cheap control by >=5 absolute percentage points or if verifier overhead eliminates CPU speedup despite adequate agreement.

## Evidence references

- Artifact root: `<local-path>/projects/learned-tiny-ternary-draft-against-a-small-cpu-transformer-d507774f6d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

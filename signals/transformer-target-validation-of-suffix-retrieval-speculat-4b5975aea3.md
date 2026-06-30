# Transformer-target validation of suffix-retrieval speculative drafts

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `transformer-target-validation-of-suffix-retrieval-speculat-4b5975aea3`
Run ID: `transformer-target-validation-of-suffix-retrieval-speculat-4b5975aea3-20260602T173613654835+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Direct Small-LM Speculative Decoding With Suffix Retrieval Drafts: enoch://control-plane/projects/direct-small-lm-speculative-decoding-with-suffix-retrieval-32ba99342c/runs/direct-small-lm-speculative-decoding-with-suffix-retrieval-32ba99342c-20260601T091000918895+0000
- Parent run decision: Transformer Speculative Decoding With Suffix Retrieval Drafts: enoch://control-plane/projects/transformer-speculative-decoding-with-suffix-retrieval-dra-ea0f941a5c/runs/transformer-speculative-decoding-with-suffix-retrieval-dra-ea0f941a5c-20260602T132000452896+0000

## What looked useful

Pythia-70M accepted 1.814 suffix-retrieval tokens/context versus 0.029 random and 1.346 last-token control; suffix-minus-last bootstrap 95% CI [0.311, 0.635]. DistilGPT-2 accepted 1.633 versus 0.045 random and 1.375 last-token; suffix-minus-last bootstrap 95% CI [0.135, 0.393]. Longer suffixes yielded higher acceptance, supporting the mechanism.

## Boundaries and scale limits

Validated on 512 repeated-suffix contexts per target with Pythia-70M-deduped and DistilGPT-2, horizon 8, CPU batched inference. Not validated for all-prompt coverage, sampled speculative acceptance with draft probabilities, production decoding throughput, larger instruction-tuned models, code/chat domains, or long-context serving.

## Claim scope

On WikiText-2 raw test contexts where the prompt contains a prior suffix match of at least two tokens, prompt-local suffix retrieval produces speculative draft continuations that two small transformer targets accept more often than random-prior and suffix-length-1 last-token retrieval controls under greedy target validation.

## Why it stopped

Bounded transformer-target validation supports the mechanism, but without an actual speculative decoder throughput/acceptance implementation the evidence is no-paper useful signal rather than paper-positive.

## Recommended next action

Run a bounded end-to-end speculative decoding implementation that compares suffix retrieval against no-draft decoding and a small neural draft baseline on tokens/s, accepted tokens per target forward, and quality-preserving exact target outputs.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end suffix-retrieval speculative decoding throughput validation
- Success threshold: At least 1.15x wall-clock tokens/s over no-draft decoding on repeated-suffix-covered prompts, exact greedy output identity with the target, and accepted tokens per target forward exceeding the last-token/prompt-lookup control with a bootstrap 95% CI above zero.
- Stop condition: Stop if suffix retrieval fails to produce a statistically positive tokens/s speedup over no-draft decoding or if target-output identity requires enough extra validation work to erase the accepted-token advantage.

## Evidence references

- Artifact root: `<local-path>/projects/transformer-target-validation-of-suffix-retrieval-speculat-4b5975aea3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

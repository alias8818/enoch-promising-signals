# Sparse Bigram Transition Drafting from Target Logits

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sparse-bigram-transition-drafting-from-target-logits-3984331b81ff`
Run ID: `sparse-bigram-transition-drafting-from-target-logits-3984331b81ff-20260604T121231010623+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/4b3dd5e2c185

## What looked useful

The target top-k oracle mass was high at the same sparsity (0.8077 for top-128), but the previous-token sparse table failed to recover that mass and underperformed a unigram control at the best sparse-bigram setting. The likely bottleneck is missing context, not sparse lookup capacity.

## Boundaries and scale limits

This was a bounded proxy evaluation, not end-to-end speculative decoding. It used one small target model, one held-out corpus, one-step acceptance, and previous-token-only states. It did not validate larger target models, multi-token draft chains, serving throughput, or context-enriched sparse states.

## Claim scope

On distilgpt2 over 32,896 held-out Wikitext-2 positions, a sparse previous-token transition table derived from target logits is not a useful standalone draft distribution under the one-step expected speculative-acceptance proxy; its best measured setting reached 0.0980 expected acceptance and underperformed a matched sparse unigram control at 0.1235.

## Why it stopped

Bounded direct acceptance-proxy evidence falsified the standalone previous-token sparse-bigram draft mechanism; this is an early/proxy falsification, not a full serving validation.

## Recommended next action

Stop this exact previous-token bigram-only line as a no-paper negative; a separate bounded follow-up should test context-enriched sparse states before any serving-scale implementation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Context-enriched sparse transition drafting from target logits
- Success threshold: At k <= 128, context-enriched sparse states beat sparse unigram and previous-token bigram controls by at least 0.03 absolute expected acceptance on 32k or more held-out positions without requiring a dense table over most observed suffixes.
- Stop condition: Stop if context-enriched states fail to beat sparse unigram by 0.01 absolute expected acceptance at k <= 128 or require table growth that is effectively dense over held-out suffixes.

## Evidence references

- Artifact root: `<local-path>/projects/sparse-bigram-transition-drafting-from-target-logits-3984331b81ff`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

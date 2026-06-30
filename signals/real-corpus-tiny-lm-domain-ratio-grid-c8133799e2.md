# Real-corpus tiny LM domain-ratio grid

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-corpus-tiny-lm-domain-ratio-grid-c8133799e2`
Run ID: `real-corpus-tiny-lm-domain-ratio-grid-c8133799e2-20260628T203542772284+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Domain-mixing ratio grid for tiny pretraining: enoch://control-plane/projects/domain-mixing-ratio-grid-for-tiny-pretraining-d272c8734667/runs/domain-mixing-ratio-grid-for-tiny-pretraining-d272c8734667-20260628T201921302906+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c3567575d683

## What looked useful

The three-seed grid found monotonic per-domain tradeoffs and a mixed-ratio balanced optimum: aggregate balanced NLL was 2.4485 at wiki_ratio 0.5 versus 2.5329 for all-news and 2.5675 for all-wiki.

## Boundaries and scale limits

Only two public text domains, byte-level tokenization, one tiny architecture, three seeds, and short training runs were tested. No GPT-2-small-class model, modern tokenizer, adaptive data mixer, multi-domain corpus, or long convergence run was evaluated.

## Claim scope

A 478,720-parameter byte-level causal Transformer trained on real Wikitext-2 and AG News text for 4.096M byte tokens per run shows a reproducible domain-ratio tradeoff across three seeds; wiki validation loss improves as wiki sampling increases, news validation loss worsens, and a mixed ratio around 0.5 gives the best balanced two-domain validation loss.

## Why it stopped

The local direct test supports the tiny-scale mechanism but is not publication-grade evidence because scale, tokenizer, baseline, and robustness checks are missing.

## Recommended next action

Stop this worker run as no-paper useful signal; next run should deepen with a small GPT-2-style tokenizer/model, three or more domains, longer checkpointed curves, and a fixed-ratio versus adaptive-mixer baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-style multi-domain ratio grid with adaptive baseline
- Success threshold: Adaptive or selected fixed mixing improves target-weighted validation NLL by at least 1 percent over every single-domain endpoint and is within variance across at least three seeds/checkpoints.
- Stop condition: Stop if no mixed or adaptive configuration beats the best single-domain endpoint on target-weighted held-out NLL after the planned checkpointed budget.

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-tiny-lm-domain-ratio-grid-c8133799e2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# Real-corpus tiny mixture confirmation for code/web/dialogue ratios

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-corpus-tiny-mixture-confirmation-for-code-web-dialogu-33584ec903`
Run ID: `real-corpus-tiny-mixture-confirmation-for-code-web-dialogu-33584ec903-20260630T025541848999+0000`

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

- Parent run decision: Code/web/dialogue mixture ratios for tiny pretraining: enoch://control-plane/projects/code-web-dialogue-mixture-ratios-for-tiny-pretraining-e2a5a9936384/runs/code-web-dialogue-mixture-ratios-for-tiny-pretraining-e2a5a9936384-20260630T023924028677+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/1c0250eb2d34

## What looked useful

Domain-heavy mixtures won their matching validation domain in 3/3 seeds for code, web, and dialogue. Equal mixture won best average validation loss in 3/3 seeds. Mean heavy-minus-equal deltas were -0.07095 nats/byte on code, -0.03611 on web, and -0.05462 on dialogue.

## Boundaries and scale limits

Only 320k train characters and 64k validation characters per domain, 260 steps per model, byte-level tokenization, tiny 4-layer/128-width models, three seeds, and narrow source choices; not evidence for large LLM pretraining ratios or assistant-quality downstream behavior.

## Claim scope

Across three seeds in a tiny byte-level causal Transformer trained on real code, web, and dialogue corpora, increasing a domain's mixture ratio from one-third to 60% consistently reduced held-out byte-level validation loss for that same domain, while the equal mixture had the best average loss across domains.

## Why it stopped

This run produced a reproducible small-scale useful signal, but it is byte-level and tiny-model evidence rather than publication-grade validation of real LLM mixture ratios.

## Recommended next action

Run a bounded deepen experiment with a standard subword tokenizer, GPT-2-small-class or parameter-matched baseline, at least five seeds, and independent held-out corpora before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Subword GPT-2-small-class confirmation of code/web/dialogue mixture-ratio specialization
- Success threshold: Each domain-heavy mixture wins its matching domain in at least 4/5 seeds and improves mean matching-domain validation loss by at least 0.02 nats/token or an explicitly justified equivalent threshold, without catastrophic average-loss degradation.
- Stop condition: Stop if domain-heavy wins occur in fewer than 3/5 seeds for any domain or if the effect vanishes under subword tokenization and independent held-out corpora.

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-tiny-mixture-confirmation-for-code-web-dialogu-33584ec903`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

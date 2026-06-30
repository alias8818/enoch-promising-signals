# N-gram context draft without model VRAM

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-context-draft-without-model-vram-11986445092b`
Run ID: `n-gram-context-draft-without-model-vram-11986445092b-20260608T085632688844+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/1b9c9a573847

## What looked useful

Context-only n-gram drafting has measurable exact-match signal, especially with larger context windows, but word-token draft runs are short and full 8-token acceptance is below 1%, so this is useful mechanism evidence rather than a paper-ready result.

## Boundaries and scale limits

Proxy-only small-corpus test; no real LLM verifier, no production BPE tokenizer, no end-to-end speculative decoding latency, no GPU/CPU overlap measurement, and no large or diverse benchmark corpus.

## Claim scope

On two small public text corpora, a CPU-side context-only n-gram index can draft exact held-out continuation tokens without a draft model in VRAM; best word/punctuation-token result was 0.42005 next-token exact accuracy and 0.69835 accepted draft tokens per position with an 8192-token context.

## Why it stopped

Stopped after a bounded proxy confirmation: the result supports a mechanism but does not directly validate real speculative-decoding speedup or target-model acceptance.

## Recommended next action

Run a bounded GPT-2-small verifier-loop follow-up using the model tokenizer and compare end-to-end greedy decoding throughput against CPU n-gram speculative drafting.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small verifier test for CPU context n-gram drafting
- Success threshold: At least 1.2x end-to-end tokens/s over greedy GPT-2-small decoding with identical generated output on the scoped benchmark and no draft model VRAM.
- Stop condition: Stop if accepted tokens per verifier step remains below 0.5 or end-to-end throughput is not improved after CPU overhead is included.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-context-draft-without-model-vram-11986445092b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

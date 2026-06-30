# SuffixTree-Spec: Prompt-Suffix Drafting Without Draft-Model VRAM

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffixtree-spec-prompt-suffix-drafting-without-draft-model-vram-64dacf813909`
Run ID: `suffixtree-spec-prompt-suffix-drafting-without-draft-model-vram-64dacf813909-20260609T123955264017+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/7332396d4975

## What looked useful

Default deterministic suffix drafting accepted 96.84% of exact copied-span target tokens and 68.85% of periodically perturbed copied-span tokens, but only 2.57% of ordinary continuation tokens. A min-match sweep showed shorter anchors increase coverage while making proposals noisier.

## Boundaries and scale limits

Tested only as an oracle simulator over 120 WikiText token windows with GPT-2 tokenization, 512-token prompts, 128-token targets, 16-token drafts, and no real target-model verifier, GPU serving loop, KV-cache measurement, or instruction-task benchmark.

## Claim scope

Prompt-only suffix drafting can accept a large fraction of tokens for exact or lightly perturbed copy-heavy outputs in a CPU oracle simulator, but it has very low coverage on ordinary WikiText continuation.

## Why it stopped

Closed as no-paper useful signal: local oracle simulation supports the copy-heavy mechanism but early-falsifies broad general-purpose usefulness and lacks real serving-speed evidence.

## Recommended next action

Run a bounded real target-model speculative decoding benchmark on copy-heavy instruction tasks, comparing latency, accepted tokens, verifier overhead, and output quality against no-draft decoding and a small draft-model baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Model Latency Test for Prompt-Suffix Drafting on Copy-Heavy Tasks
- Success threshold: At least 15% median wall-clock latency reduction versus no-draft decoding on copy-heavy tasks, no quality regression, and lower peak VRAM than a draft-model baseline.
- Stop condition: Stop if accepted-token fraction is below 25% on copy-heavy tasks or verifier/proposal overhead eliminates latency gains in the first bounded benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/suffixtree-spec-prompt-suffix-drafting-without-draft-model-vram-64dacf813909`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

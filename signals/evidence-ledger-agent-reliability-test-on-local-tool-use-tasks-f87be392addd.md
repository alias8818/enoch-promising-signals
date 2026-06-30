# Evidence-Ledger Agent Reliability Test on Local Tool-Use Tasks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-agent-reliability-test-on-local-tool-use-tasks-f87be392addd`
Run ID: `evidence-ledger-agent-reliability-test-on-local-tool-use-tasks-f87be392addd-20260609T134717601189+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ca73369961ca

## What looked useful

Evidence-ledger prompting converted correct-but-sometimes-unstructured local observation answers into fully machine-checkable answer-plus-evidence outputs with about 0.51 seconds/request added mean latency, but this easy benchmark does not show factual accuracy gains.

## Boundaries and scale limits

Single local quantized model, 24 synthetic controller-supplied observation tasks, no autonomous tool planning, CPU-only llama.cpp build despite GB10 host, no multi-model or held-out repository validation.

## Claim scope

On 24 generated local tool-observation tasks using Phi-4-mini-instruct-Q4_K_M through llama.cpp, evidence-ledger prompting produced parseable answers with complete cited observation support on every task; it did not improve lenient factual answer accuracy because both baseline and ledger outputs contained the correct answer on all tasks.

## Why it stopped

No-paper useful signal: the local benchmark supports schema/evidence observability, but not an answer-accuracy improvement or publication-grade agent reliability claim.

## Recommended next action

Run a bounded deepen benchmark with harder adversarial local-tool tasks and compare evidence-ledger prompting against a baseline that is also required to emit citation IDs.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adversarial Evidence-Ledger Benchmark with Citation-Schema Control
- Success threshold: Ledger workflow beats the citation-schema baseline by at least 10 percentage points on exact-and-supported answers or reduces unsupported wrong answers by at least 30% without lowering exact answer accuracy by more than 2 percentage points.
- Stop condition: Stop as negative if both methods are within 5 percentage points on exact-and-supported answers and unsupported wrong-answer rate after 100 tasks, or if task difficulty fails to produce at least 10 total baseline errors.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-reliability-test-on-local-tool-use-tasks-f87be392addd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
